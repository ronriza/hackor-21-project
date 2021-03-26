import requests
import json
import pandas


response = requests.get("https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers")

print (json.dumps(response.json(), indent=4, sort_keys=True))

data=json.dumps(response.json(), indent=4, sort_keys=True)
csv_output_obj=pandas.read_json(data, orient="columns")
csv_output_obj.to_csv('data.csv')
