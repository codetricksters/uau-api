from uau_api import UauAPI

API_URL = "https://gamma-api.seniorcloud.com.br:51938/uauAPI/api/v1.0/"
API_KEY = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..Bt9qF2Zqp3x7JnjSAq_rVw.ddUPc8T5CE9xUiCrcM0FJ-F_FNjHnic9DpZvnLNMk2_eaaxihFnCF-WxurpX9XauunecIuPMw5N_qnp9fZrZR2XYqyO5wa_Oj8NjH84-KCPpa2tSoauAgnk7MaVJJLEcq-0lVTRSD5LGy6pH8hrkDlmadgltmvEMr8xySbbg2zc.W_lju2PmOvOvdLc109jqig"
LOGIN = "autoproc"
PASSWORD = "hybr12"

uau = UauAPI(base_url=API_URL, api_key=API_KEY)
uau.authenticate(LOGIN, PASSWORD)

response = uau.Obras.obter_obras_ativas()
print(response.status_code)
print(response.json())
