"""Base API client module."""
import requests
from typing import Optional, Dict, Any

class BaseAPI:
    """Base class for API client implementation."""
    
    def __init__(self, base_url: str, api_key: str, session: Optional[requests.Session] = None):
        """Initialize the API client.
        
        Args:
            base_url: The base URL for the API
            session: Optional session to use for requests
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = session or requests.Session()
    
    def _request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        """Make an HTTP request to the API.
        
        Args:
            method: HTTP method (get, post, etc)
            path: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def get(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make a GET request."""
        return self._request('GET', path, **kwargs)
    
    def post(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make a POST request."""
        return self._request('POST', path, **kwargs)
    
    def put(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make a PUT request."""
        return self._request('PUT', path, **kwargs)
    
    def delete(self, path: str, **kwargs) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self._request('DELETE', path, **kwargs)