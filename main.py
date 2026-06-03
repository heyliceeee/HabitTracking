import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{user_param['username']}/graphs"
graph_param = {
    "id": "daily-water",
    "name": "Daily Hydration",
    "unit": "L",
    "type": "float",
    "color": "ajisai"
}
headers = {"X-USER-TOKEN": TOKEN}

response = requests.post(graph_endpoint, json=graph_param, headers=headers)
print(response.text)