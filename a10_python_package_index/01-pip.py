# ********** PIP ****************
import requests

response = requests.get("http://google.com")
print(response)             # <Response [200]>, meaning success
