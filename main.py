import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

headers = {"X-USER-TOKEN": TOKEN}
pixela_endpoint = "https://pixe.la/v1/users"

# Create user
user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#requests.post(url=pixela_endpoint, json=user_body)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{user_body['username']}/graphs"
graph_body = {
    "id": "daily-water",
    "name": "Daily Hydration",
    "unit": "L",
    "type": "float",
    "color": "ajisai"
}
#requests.post(url=graph_endpoint, json=graph_body, headers=headers)

# Add pixel
pixel_endpoint = f"{graph_endpoint}/daily-water"
add_pixel_body = {
    "date": datetime.datetime.now().strftime("%Y%m%d"),
    "quantity": "1.5"
}
#requests.post(url=pixel_endpoint, json=add_pixel_body, headers=headers)

# Update pixel
update_pixel_endpoint = f"{pixel_endpoint}/{add_pixel_body['date']}"
update_pixel_body = {
    "quantity": "1.0"
}
#requests.put(url=update_pixel_endpoint, json=update_pixel_body, headers=headers)
