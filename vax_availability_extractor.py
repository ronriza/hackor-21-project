import requests
import json
import pandas


# request list of vaccine providers in NY from the am-i-eligible API
response = requests.get("https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers")


# prints am-i-eligible json
#print(json.dumps(response.json()['providerList'], indent=4, sort_keys=True))

data=json.dumps(response.json()['providerList'], indent=4, sort_keys=True)
csv_output_obj=pandas.read_json(data, orient="columns")
csv_output_obj.to_csv('data.csv')


"""The following code gathers lat/long from zip code api then uses that lat/long info on the vaccinefinder.org api"""


# insert user's zip code here, perhaps this could be a variable
zip_code="60618"
# insert Fahad's zip code api key here from the requirements document or configure as environmental variable
api_key=""
zip_code_URL = "https://www.zipcodeapi.com/rest/"+api_key+"/info.json/"+zip_code+"/degrees"


# sending get request and saving the response as response object
zip_code_request = requests.get(url=zip_code_URL)

# extracting data in json format
zip_code_json_data = zip_code_request.json()
# received latitude coordinates
latitude=zip_code_json_data["lat"]
# received longitude coordinates
longitude=zip_code_json_data["lng"]
#print(zip_code_data)
#print(latitude, longitude)

# pretending we are the Postman
headers_list ={"User-Agent": 'PostmanRuntime/7.26.10'}

# api endpoint url
castlight_url="https://api.us.castlighthealth.com/vaccine-finder/v1/provider-locations/search"

# query parameters, search radius can be changed
parameters={"medicationGuids":"779bfe52-0dd8-4023-a183-457eb100fccc,a84fb9ed-deb4-461c-b785-e17c782ef88b,784db609-dc1f-45a5-bad6-8db02e79d44f",
        "lat":latitude,
        "long":longitude,
        "radius":10}


# send api request
castlight_api_data=requests.get(url=castlight_url, params=parameters, headers=headers_list, timeout=30)
castlight_json_data=castlight_api_data.json()
print(json.dumps(castlight_json_data, indent=4, sort_keys=True))

# get the providers list of dictionaries and sort (thanks Ron for help with previous example)
castlight_providers=json.dumps(castlight_json_data['providers'], indent=4, sort_keys=True)
# create panda object
castlight_csv_obj=pandas.read_json(castlight_providers, orient="columns")
# write to csv
castlight_csv_obj.to_csv('vaccineFinder.csv')

# TODO: instead of rewriting entire file, append add to file when we make an api call. Also try to only have 1 csv file with all data?