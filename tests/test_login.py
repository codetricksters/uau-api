"""Test module for UAU API login functionality.

This module tests the login functionality of the UAU API client.
It loads configuration from environment variables using python-dotenv.
"""

import os
import pytest
from dotenv import load_dotenv
from uau_api.settings import Settings
from uau_api.client import UauAPI


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Load environment variables from .env file before running tests."""
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    load_dotenv(env_path)


@pytest.fixture
def settings():
    """Create Settings instance from environment variables."""
    return Settings()


@pytest.fixture
def api_client(settings):
    """Create an API client instance for testing."""
    return UauAPI(base_url=settings.API_URL, api_key=settings.API_KEY)


class TestLogin:
    """Test suite for login functionality."""

    def test_settings_loaded_from_env(self, settings):
        """Test that settings are correctly loaded from environment variables."""
        assert settings.API_URL, "API_URL not set in environment"
        assert settings.API_KEY, "API_KEY not set in environment"
        assert settings.USERNAME, "USERNAME not set in environment"
        assert settings.PASSWORD, "PASSWORD not set in environment"

    def test_api_url_format(self, settings):
        """Test that API_URL is in a valid format."""
        assert settings.API_URL.startswith("http://") or settings.API_URL.startswith(
            "https://"
        ), "API_URL must start with http:// or https://"

    def test_api_key_not_empty(self, settings):
        """Test that API_KEY is not empty."""
        assert len(settings.API_KEY) > 0, "API_KEY must not be empty"

    def test_username_not_empty(self, settings):
        """Test that USERNAME is not empty."""
        assert len(settings.USERNAME) > 0, "USERNAME must not be empty"

    def test_password_not_empty(self, settings):
        """Test that PASSWORD is not empty."""
        assert len(settings.PASSWORD) > 0, "PASSWORD must not be empty"

    def test_api_client_initialization(self, api_client):
        """Test that API client is properly initialized."""
        assert api_client is not None
        assert api_client.session is not None

    def test_api_client_has_authentication_header(self, api_client, settings):
        """Test that API client has the authorization header set."""
        assert "X-INTEGRATION-Authorization" in api_client.session.headers
        assert (
            api_client.session.headers["X-INTEGRATION-Authorization"]
            == settings.API_KEY
        )

    @pytest.mark.skip(
        reason="Integration test - requires live API endpoint. "
        "Unskip when testing against real API."
    )
    def test_autenticar_usuario(self, settings):
        """Integration test for authenticating a user.
        
        This test requires a live API endpoint and will be skipped by default.
        To run this test, you need a valid .env file with real credentials.
        """
        api_client = UauAPI(base_url=settings.API_URL, api_key=settings.API_KEY)
        
        # Call the autenticar_usuario method
        response = api_client.autenticador.autenticar_usuario(
            login=settings.USERNAME, senha=settings.PASSWORD
        )
        
        # Basic response validation
        assert response is not None
        assert isinstance(response, dict)
