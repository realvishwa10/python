import requests
from datetime import datetime

pixela_url = "https://pixe.la/v1/users"
USERNAME = "ghost10"
TOKEN = "dgjlsdgjqw4nm342"
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

parameters = {
    "token": "dgjlsdgjqw4nm342",
    "username": "ghost10",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_add_endpoint = f"{graph_endpoint}/graph1"

add_config = {
    "date": formatted_date,
    "quantity": "9.74"
}

# response = requests.post(url=graph_add_endpoint, json=add_config, headers=headers)
# print(response.text)

graph_update_delete_endpoint = f"{graph_add_endpoint}/{formatted_date}"

update_config = {
    "quantity": "15.0"
}

# response = requests.put(url=graph_update_delete_endpoint, json=update_config, headers=headers)

response = requests.delete(url=graph_update_delete_endpoint, headers=headers)