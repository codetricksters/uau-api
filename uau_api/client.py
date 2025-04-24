"""Main API client module."""
from typing import Dict, Any, Optional
import requests
from .requestsapi import RequestsApi

class UauAPI(RequestsApi):
    """Main API client class that provides access to all API groups."""
    
    def __init__(self, base_url: str, api_key: str, session: Optional[requests.Session] = None):
        """Initialize the API client.
        
        Args:
            base_url: The base URL for the API
            session: Optional session to use for requests
        """
        super().__init__(base_url, api_key, session)
        self.is_authenticated = False
        self._init_api_groups()
        self.session.headers['X-INTEGRATION-Authorization'] = api_key

    def _init_api_groups(self):
        """Initialize API group classes."""
        # Import all group classes
        from .groups.acompanhamentos_servicos import AcompanhamentosServicos
        from .groups.anexo import Anexo
        from .groups.obras import Obras
        
        # Initialize group instances
        self.AcompanhamentosServicos = AcompanhamentosServicos(self)
        self.Anexo = Anexo(self)
        self.Obras = Obras(self)

    def authenticate(self, username: str, password: str) -> Dict[str, Any]:
        """Authenticate with the API.
        
        Args:
            username: API username
            password: API password
        
        Returns:
            Authentication response data
        """
        auth_response = self.post(
            "Autenticador/AutenticarUsuario",
            json={"Login": username, "Senha": password}
        )
        self.session.headers['Authorization'] = auth_response.json()
        self.is_authenticated = True
        return auth_response
        
    def get_session(self) -> requests.Session:
        """Get the current session.
        
        Returns:
            The requests Session object
        """
        return self.session