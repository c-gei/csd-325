import json
import requests
## TEST:
##response = requests.get("http://www.google.com")
##print(response.status_code)

## Retrieving current astronauts and formatting output 
##response = requests.get("http://api.open-notify.org/astros")
##print(response.status_code)
##print(response.json())

## My own program
response = requests.get("https://api-server.dataquest.io/economic_data/countries") 
print(response.status_code)

data = json.loads(response.json())
print(f"Total countries: {len(data)}")
print(f"First country: {data[0]['short_name']}")
