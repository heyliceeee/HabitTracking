import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token": "fdnmfoneof",
    "username": "heyliceeee",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_param) # post request
print(response.text)