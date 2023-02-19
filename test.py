import requests

res = requests.get("http://localhost:5000/image?width=100&height=100")
print(res.status_code)
print(res.text)
