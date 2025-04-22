# http://docs.python-requests.org/en/master/api/
import requests
from requests.compat import urljoin

class RequestsApi:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def request(self, method, url, **kwargs):
        return self.session.request(method, urljoin(self.base_url, url), **kwargs)

    def head(self, url, **kwargs):
        return self.session.head( urljoin(self.base_url, url), **kwargs)

    def get(self, url, **kwargs):
        return self.session.get( urljoin(self.base_url, url), **kwargs)

    def post(self, url, **kwargs):
        return self.session.post( urljoin(self.base_url, url), **kwargs)

    def put(self, url, **kwargs):
        return self.session.put( urljoin(self.base_url, url), **kwargs)

    def patch(self, url, **kwargs):
        return self.session.patch( urljoin(self.base_url, url), **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete( urljoin(self.base_url, url), **kwargs)

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination