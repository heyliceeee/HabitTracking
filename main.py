import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

headers = {"X-USER-TOKEN": TOKEN}
pixela_endpoint = "https://pixe.la/v1/users"
user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{user_body['username']}/graphs"
graph_body = {
    "id": "daily-water",
    "name": "Daily Hydration",
    "unit": "L",
    "type": "float",
    "color": "ajisai"
}

add_pixel_endpoint = f"{graph_endpoint}/daily-water"
add_pixel_body = {
    "date": datetime.datetime.now().strftime("%Y%m%d"),
    "quantity": "1.5"
}
response = requests.post(url=add_pixel_endpoint, json=add_pixel_body, headers=headers)
