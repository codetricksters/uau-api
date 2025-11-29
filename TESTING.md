# Login Test Setup Documentation

## Overview
A comprehensive login test suite has been set up for the UAU API project using environment variables from a `.env` file to manage sensitive credentials.

## Files Created/Modified

### 1. `.env.example` (New File)
**Location:** `/home/leonardoalves/pyprojects/uau-api/.env.example`

This is a template file showing what environment variables are needed:
```
API_URL=https://api.example.com
API_KEY=your_api_key_here
USERNAME=your_username_here
PASSWORD=your_password_here
```

**Usage:** Copy this file to `.env` and fill in your actual values. The `.env` file will be ignored by git.

### 2. `tests/test_login.py` (New File)
**Location:** `/home/leonardoalves/pyprojects/uau-api/tests/test_login.py`

Comprehensive test module with the following features:

#### Fixtures:
- `load_env()`: Automatically loads environment variables from `.env` at session start
- `settings()`: Provides a Settings instance with loaded credentials
- `api_client()`: Provides an initialized UauAPI client

#### Test Cases:
- `test_settings_loaded_from_env`: Verifies all required environment variables are set
- `test_api_url_format`: Validates API_URL starts with http:// or https://
- `test_api_key_not_empty`: Ensures API_KEY is provided
- `test_username_not_empty`: Ensures USERNAME is provided
- `test_password_not_empty`: Ensures PASSWORD is provided
- `test_api_client_initialization`: Verifies API client is properly initialized
- `test_api_client_has_authentication_header`: Checks that authorization header is set
- `test_autenticar_usuario`: Integration test (skipped by default) for live API testing

### 3. `pyproject.toml` (Modified)
**Location:** `/home/leonardoalves/pyprojects/uau-api/pyproject.toml`

Added `python-dotenv>=1.0.0` to dev dependencies for `.env` file support.

### 4. `.gitignore` (Already Configured)
**Location:** `/home/leonardoalves/pyprojects/uau-api/.gitignore` (Line 142)

Confirmed that `.env` is already listed in `.gitignore` to prevent accidental commits of sensitive data.

## Security Best Practices Implemented

✅ `.env` file is in `.gitignore` - prevents accidental commit of secrets
✅ `.env.example` is committed - shows structure without sensitive values
✅ Settings are loaded via pydantic-settings with `env_file` configuration
✅ Sensitive credentials are never hardcoded
✅ Tests can run with any environment by providing `.env` variables

## Setup Instructions

1. **Copy the template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your credentials:**
   ```bash
   nano .env
   # or your preferred editor
   ```

3. **Install dependencies:**
   ```bash
   pip install python-dotenv
   ```

4. **Run the tests:**
   ```bash
   pytest tests/test_login.py -v
   ```

5. **Run only validation tests (no integration tests):**
   ```bash
   pytest tests/test_login.py -v -m "not skip"
   ```

## Test Execution Examples

```bash
# Run all tests
task test

# Run only login tests
pytest tests/test_login.py -v

# Run with coverage
pytest tests/test_login.py --cov=uau_api -v

# Run specific test
pytest tests/test_login.py::TestLogin::test_settings_loaded_from_env -v
```

## Integration Test (Optional)

The `test_autenticar_usuario` test is marked as skipped by default. To run it:

1. Ensure your `.env` file has valid API credentials
2. Run with unskip flag:
   ```bash
   pytest tests/test_login.py::TestLogin::test_autenticar_usuario -v -s
   ```

## Environment Variables Required

| Variable | Purpose | Example |
|----------|---------|---------|
| `API_URL` | Base URL for the API | `https://api.example.com` |
| `API_KEY` | Authentication API key | (your api key) |
| `USERNAME` | User login credentials | (your username) |
| `PASSWORD` | User password | (your password) |

## Important Notes

⚠️ **CRITICAL:** Never commit the `.env` file to version control!
⚠️ Never share your `.env` file or copy its contents to chat/email
✅ Always use `.env.example` to share the structure with team members
✅ Use CI/CD secrets management (GitHub Secrets, etc.) for automated deployments

## References

- [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [Pytest Fixtures](https://docs.pytest.org/en/stable/how-to_api/fixtures.html)
