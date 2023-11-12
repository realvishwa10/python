import requests
response = requests.get("https://api.npoint.io/a557423de18f51f4678f")
print(response)
print(response.json())
