import requests
req = requests.get('http://google.com')
print(req.status_code)
