import requests
import json

response = requests.get("https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers")

print (json.dumps(response.json(), indent=4, sort_keys=True))

