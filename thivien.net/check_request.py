import requests

r = requests.get("https://www.thivien.net/")
print(r.status_code)