from uau_api import catalog


def test_catalog_size_and_groups():
    assert len(catalog.load_catalog()) == 431
    assert len(catalog.groups()) == 51


def test_paths_are_relative_without_version():
    for e in catalog.load_catalog():
        assert not e.path.startswith('/')
        assert 'v{version}' not in e.path


def test_unversioned_paths_go_one_level_up():
    ep = catalog.get('cotacao', 'ContaCotacoesMob')
    assert ep.path == '../Cotacao/ContaCotacoesMob'


def test_lookup_is_case_and_separator_insensitive():
    a = catalog.get('Obras', 'ObterObrasAtivas')
    b = catalog.get('obras', 'obter-obras-ativas')
    assert a is not None and a == b
    assert a.path == 'Obras/ObterObrasAtivas'


def test_path_params_and_name():
    ep = catalog.get('chave-pix', 'consultar')
    assert ep.method == 'GET'
    assert ep.path_params == ['cpfCnpj']


def test_auth_headers_and_version_are_not_params():
    for e in catalog.load_catalog():
        names = {p['name'] for p in e.params}
        assert not names & {
            'version',
            'Authorization',
            'X-INTEGRATION-Authorization',
        }


def test_search_requires_all_terms():
    assert all(
        'obras' in kebab_hay
        for kebab_hay in (
            e.group.lower() for e in catalog.search('obras ativas')
        )
    )
    assert catalog.search('zzzz-nao-existe') == []


def test_kebab():
    assert catalog.kebab('ObterObrasAtivas') == 'obter-obras-ativas'
    assert catalog.kebab('login_usuario') == 'login-usuario'
