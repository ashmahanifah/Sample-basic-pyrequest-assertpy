import requests

req = requests.delete("https://reqres.in/api/users/2")


print(req.status_code) #expected 204