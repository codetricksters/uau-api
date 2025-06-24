from requests import Session
from requests.compat import urljoin
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class RequestsApi:
    """Cls doc"""
    def __init__(self, base_url, api_key: str, session=None, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        if session:
            self.session = session
        else:
            # Create a new session only if one wasn't provided
            self.session = Session()
            # Configure retry strategy for new sessions
            retry_strategy = Retry(
                total=1,
                backoff_factor=1,
                status_forcelist=[408, 429, 500, 502, 503, 504],
                allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "POST", "PATCH"]
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)
        
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def get_session(self):
        """Get the current session for use by other classes"""
        return self.session

    def get_headers(self):
        """Get the current headers with auth token for use by other classes"""
        return self.session.headers.copy()

    def request(self, method, url, **kwargs):
        return self.session.request(method, urljoin(self.base_url, url), **kwargs)

    def head(self, url, **kwargs):
        return self.session.head(urljoin(self.base_url, url), **kwargs)

    def get(self, url, **kwargs):
        return self.session.get(urljoin(self.base_url, url), **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(urljoin(self.base_url, url), **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(urljoin(self.base_url, url), **kwargs)

    def patch(self, url, **kwargs):
        return self.session.patch(urljoin(self.base_url, url), **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(urljoin(self.base_url, url), **kwargs)

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination