import requests
import json

# request list of vaccine providers in NY from the am-i-eligible API
response = requests.get("https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers")

# prints am-i-eligible json
print(json.dumps(response.json(), indent=4, sort_keys=True))

