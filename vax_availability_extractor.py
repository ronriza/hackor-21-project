import requests
import json
import pandas


# request list of vaccine providers in NY from the am-i-eligible API
response = requests.get("https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers")


# prints am-i-eligible json
print(json.dumps(response.json()['providerList'], indent=4, sort_keys=True))

data=json.dumps(response.json()['providerList'], indent=4, sort_keys=True)
csv_output_obj=pandas.read_json(data, orient="columns")
csv_output_obj.to_csv('data.csv')
