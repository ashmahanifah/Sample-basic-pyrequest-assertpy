from pprint import pprint

import requests

payload = {
    "name": "Reyn Agatha",
    "gender": "female",
    "email": "reynagatha13@gmail.com",
    "status": "active"
}

headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer 9cacd99cde1899178349371cb10bc4fb1ee0c1c0d8fcb2712b6b72bbeb380b18"
}

req_createuser = requests.post("https://gorest.co.in/public/v2/users", json=payload, headers=headers)
resp_createuser = req_createuser.json()

pprint(resp_createuser)

print(req_createuser.status_code) #expected 201

id_user = resp_createuser["id"]

print(id_user)

#=============== Delete user =================#

# req_delete = requests.delete(f"https://gorest.co.in/public/v2/users/{id_user}", headers=headers)
#
# print(req_delete.status_code) #expected 204