import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}

req_createuser = requests.post("https://reqres.in/api/users", json=payload)
resp_createuser = req_createuser.json()

print(req_createuser.status_code) #expected 201

