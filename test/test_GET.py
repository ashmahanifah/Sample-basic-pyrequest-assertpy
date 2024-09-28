from pprint import pprint

import requests

req = requests.get("https://reqres.in/api/users?page=2")
resp = req.json()

pprint(resp)

# sup_url = resp.get("support")["url"]

# print(sup_url)
print(req.status_code) #expected 200

print(req.elapsed.microseconds/1000)