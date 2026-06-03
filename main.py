import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

headers = {"X-USER-TOKEN": TOKEN}
pixela_endpoint = "https://pixe.la/v1/users"

def create_user(token, username):
    """Create a user if not exists"""
    body = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    requests.post(url=pixela_endpoint, json=body)
def create_graph(username, graph_id, graph_name, graph_unit, graph_type, graph_color):
    """Create a graph if not exists"""
    endpoint = f"{pixela_endpoint}/{username}/graphs"
    body = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": graph_type,
        "color": graph_color
    }
    requests.post(url=endpoint, json=body, headers=headers)
def update_pixel(username, graph_id, date):
    """Update pixel"""
    endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
    quantity = input("How many liters did you drink today? (float)")
    body = {
        "quantity": quantity
    }
    requests.put(url=endpoint, json=body, headers=headers)
def delete_pixel(username, graph_id, date):
    """Delete pixel"""
    endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
    print("Deleting today's pixel...")
    requests.delete(url=endpoint, headers=headers)

#create_user(TOKEN, USERNAME)
#create_graph(TOKEN, USERNAME, "daily-water", "Daily Hydration", "L", "float", "ajisai")

date = datetime.datetime.now().strftime("%Y%m%d")
while True:
    print("Choose an option: ")
    print("1. Create/Update today's pixel")
    print("2. Delete today's pixel")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        update_pixel(USERNAME, "daily-water", date) # Update pixel

    elif choice == "2":
        delete_pixel(USERNAME, "daily-water", date) # Delete pixel

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")