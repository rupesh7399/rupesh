import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjEzNjQzMTgzLCJqdGkiOiIxMDc0M2Y0NGM0ZDY0OGI4YjA0YjhkNzRkNTY1MDMyZiIsInVzZXJfaWQiOjR9.AT44kA6MigaFb4tDCU8lo_V5RM6RXBIX3mcgAvunDis'
r = requests.get('http://localhost:8000/Task/t1task/', headers = headers )
print(r.text)