import json
import os
import stat
import sys

import pytest
from typer.testing import CliRunner

from uau_api.cli import config as cfgmod
from uau_api.cli import main as climod
from uau_api.cli.config import CliConfig, ConfigError, load_config, save_config

runner = CliRunner()


class FakeResp:
    def __init__(self, status=200, data=None):
        self.status_code = status
        self._data = data

    @property
    def ok(self):
        return self.status_code < 400

    def json(self):
        if self._data is None:
            raise ValueError
        return self._data

    @property
    def text(self):
        return json.dumps(self._data)


@pytest.fixture
def fake_api(monkeypatch):
    calls = {}

    class FakeAPI:
        def __init__(self, base_url, api_key, session=None):
            calls['init'] = (base_url, api_key)

        def authenticate(self, username, password):
            calls['auth'] = (username, password)
            return calls.get('auth_resp', FakeResp(200, 'tok'))

        def request(self, method, url, **kw):
            calls['request'] = (method, url, kw)
            return calls.get('resp', FakeResp(200, {'ok': True}))

    monkeypatch.setattr('uau_api.client.UauAPI', FakeAPI)
    return calls


@pytest.fixture
def cfg_path(tmp_path):
    return tmp_path / 'config.toml'


def invoke(cfg_path, *args, **kw):
    return runner.invoke(climod.app, ['--config', str(cfg_path), *args], **kw)


def test_save_config_is_0600_and_roundtrips(cfg_path):
    save_config(
        cfg_path, CliConfig('https://h/api/v1/', 'tok"en', 'u', 'p\\w')
    )
    if os.name == 'posix':
        assert stat.S_IMODE(cfg_path.stat().st_mode) == 0o600
    cfg = load_config(cfg_path)
    assert (cfg.api_key, cfg.username, cfg.password) == ('tok"en', 'u', 'p\\w')


def test_secrets_not_in_repr(cfg_path):
    cfg = CliConfig('u', 'SECRETTOKEN', 'x', 'SECRETPASS')
    assert 'SECRET' not in repr(cfg)


def test_missing_token_is_an_error(cfg_path):
    cfg_path.write_text('api_url = "https://h/"\n')
    with pytest.raises(ConfigError, match='api_key'):
        load_config(cfg_path)


def test_no_password_or_token_flags_exist():
    result = runner.invoke(
        climod.app, ['obras', 'obter-obras-ativas', '--help']
    )
    assert '--password' not in result.output and '--senha' not in result.output
    assert '--password' not in runner.invoke(climod.app, ['--help']).output


def test_config_show_masks_secrets(cfg_path):
    save_config(
        cfg_path, CliConfig('https://h/', 'SECRETTOKEN', 'u', 'SECRETPASS')
    )
    result = invoke(cfg_path, 'config', 'show')
    assert result.exit_code == 0
    assert 'SECRET' not in result.output


def test_command_without_config_fails(cfg_path, fake_api):
    result = invoke(cfg_path, 'obras', 'obter-obras-ativas')
    assert result.exit_code == 2
    assert 'config init' in result.output


def test_password_prompted_when_not_in_file(cfg_path, fake_api, monkeypatch):
    save_config(cfg_path, CliConfig('https://h/api/v1', 'tok', 'joao'))
    monkeypatch.setattr(cfgmod.getpass, 'getpass', lambda prompt='': 's3cret')
    result = invoke(cfg_path, 'obras', 'obter-obras-ativas')
    assert result.exit_code == 0, result.output
    assert fake_api['auth'] == ('joao', 's3cret')
    assert fake_api['init'] == ('https://h/api/v1/', 'tok')
    assert 's3cret' not in result.output


def test_username_prompted_when_missing(cfg_path, fake_api, monkeypatch):
    save_config(cfg_path, CliConfig('https://h/', 'tok'))
    monkeypatch.setattr(cfgmod.getpass, 'getpass', lambda prompt='': 'pw')
    result = invoke(cfg_path, 'obras', 'obter-obras-ativas', input='maria\n')
    assert result.exit_code == 0, result.output
    assert fake_api['auth'] == ('maria', 'pw')


def test_credentials_from_file_do_not_prompt(cfg_path, fake_api, monkeypatch):
    save_config(cfg_path, CliConfig('https://h/', 'tok', 'u', 'p'))
    monkeypatch.setattr(
        cfgmod.getpass, 'getpass', lambda prompt='': pytest.fail('prompted')
    )
    assert invoke(cfg_path, 'obras', 'obter-obras-ativas').exit_code == 0
    assert fake_api['auth'] == ('u', 'p')


def test_auth_rejected_exits_1_and_skips_request(cfg_path, fake_api):
    save_config(cfg_path, CliConfig('https://h/', 'tok', 'u', 'p'))
    fake_api['auth_resp'] = FakeResp(401, 'no')
    result = invoke(cfg_path, 'obras', 'obter-obras-ativas')
    assert result.exit_code == 1
    assert 'request' not in fake_api


def test_http_error_exits_1(cfg_path, fake_api):
    save_config(cfg_path, CliConfig('https://h/', 'tok', 'u', 'p'))
    fake_api['resp'] = FakeResp(500, {'erro': 'x'})
    assert invoke(cfg_path, 'obras', 'obter-obras-ativas').exit_code == 1


def test_body_merges_options_over_json(cfg_path, fake_api):
    from uau_api import catalog

    ep = next(
        e
        for e in catalog.load_catalog()
        if e.body
        and e.body['type'] == 'object'
        and any(p['type'] == 'string' for p in e.body['properties'])
    )
    prop = next(p for p in ep.body['properties'] if p['type'] == 'string')[
        'name'
    ]
    save_config(cfg_path, CliConfig('https://h/', 'tok', 'u', 'p'))
    result = invoke(
        cfg_path,
        '--raw',
        climod.kebab(ep.group),
        climod.kebab(ep.name),
        '--body',
        json.dumps({prop: 'old', 'extra': 1}),
        f'--{climod.kebab(prop)}',
        'new',
    )
    assert result.exit_code == 0, result.output
    method, url, kw = fake_api['request']
    assert kw['json'] == {prop: 'new', 'extra': 1}
    assert url == ep.path


def test_path_param_is_substituted_and_quoted(cfg_path, fake_api):
    save_config(cfg_path, CliConfig('https://h/', 'tok', 'u', 'p'))
    result = invoke(cfg_path, 'chave-pix', 'consultar', '--cpf-cnpj', 'a/b')
    assert result.exit_code == 0, result.output
    assert fake_api['request'][1] == 'ChavePix/Pessoas/Consultar/a%2Fb'
    assert fake_api['request'][0] == 'GET'


def test_describe_and_search():
    assert (
        runner.invoke(
            climod.app, ['describe', 'obras', 'obter-obras-ativas']
        ).exit_code
        == 0
    )
    assert (
        runner.invoke(climod.app, ['describe', 'obras', 'nope']).exit_code == 2
    )
    assert (
        'obter-obras-ativas'
        in runner.invoke(climod.app, ['search', 'obras', 'ativas']).output
    )
