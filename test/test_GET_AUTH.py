from pprint import pprint
import requests
from assertpy import assert_that

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer 9cacd99cde1899178349371cb10bc4fb1ee0c1c0d8fcb2712b6b72bbeb380b18"
}

id_user = "7433129"
req_getuser = requests.get(f"https://gorest.co.in/public/v2/users/{id_user}", headers=headers)
resp_getuser = req_getuser.json()

pprint(resp_getuser)

print(req_getuser.status_code)  # expected 200

user_gender = resp_getuser["gender"]
user_email = resp_getuser["email"]

#========== Assert that =============#

assert_that(user_gender).is_in('male', 'female')
assert_that(user_email).contains('@gmail')

