import requests

payload = {
    "name": "morpheus",
    "job": "QA Engineer"
}

req = requests.put("https://reqres.in/api/users/2", json=payload)
resp = req.json()

print(resp)

print(req.status_code) #expected 200

