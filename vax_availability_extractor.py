import requests
import json
import pandas
import datetime

city_to_zip = {
    "Albany, NY": 12222,
    "Corning, NY": 14830,
    "Henrietta, NY": 14467,
    "Johnson City, NY": 13902,
    "Middletown, NY": 10940,
    "Oneonta, NY": 13820,
    "Plattsburgh, NY": 12903,
    "Potsdam, NY": 13676,
    "Queensbury, NY": 12804,
    "Syracuse, NY": 13209,
    "Utica, NY": 13502,
    "Brentwood, NY": 11784,
    "Brooklyn, NY": 11225,
    "Buffalo, NY": 14215,
    "Bronx, NY": 10466,
    "Glen Head, NY": 11568,
    "Jamaica, NY": 11451,
    "New Paltz, NY": 12561,
    "New York, NY": 10001,
    "Niagara Falls, NY": 14303,
    "Rochester, NY": 14608,
    "South Ozone Park, NY": 11420,
    "Southampton, NY": 11968,
    "Stony Brook, NY": 11794,
    "Wantagh, NY": 11793,
    "White Plains, NY": 10606,
    "Yonkers, NY": 10701
}


def get_NY_vaccines():
    """Requests NY vaccine api and writes to data.csv"""

    # request list of vaccine providers in NY from the am-i-eligible API
    response = requests.get("https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers")
    # prints am-i-eligible json
    # print(json.dumps(response.json()['providerList'], indent=4, sort_keys=True))
    data = json.dumps(response.json()['providerList'], indent=4, sort_keys=True)
    # convert to string
    json_loads = json.loads(data)
    # flatten
    normalized = pandas.json_normalize(json_loads)
    # columns to drop
    drop_these_columns = ["isShowable", "providerId"]
    # drop columns
    normalized.drop(columns=drop_these_columns, inplace=True)
    # create now object
    now = datetime.datetime.now()
    # add the column to the table
    normalized["last_checked"] = now.strftime("%Y-%m-%d %H:%M:%S")
    # match cities to zip_codes
    normalized['zip_code'] = normalized['address'].map(city_to_zip)
    # write to csv
    normalized.to_csv('res/data.csv')


# def get_lat_long(zip_code_string):
#     """Gets latitude and longitutde from zip code api. Returns latitude and longitude strings."""

#     # insert zip code api key here from the requirements document or configure as environmental variable
#     api_key = "Sqd7cXx6u2q8nlmuc1epHAVujrnwFlQl8ikMQBSPwu2z2YWZ2BMto8ZDgTCAH2l7"
#     zip_code_URL = "https://www.zipcodeapi.com/rest/" + api_key + "/info.json/" + zip_code_string + "/degrees"

#     # sending get request and saving the response as response object
#     zip_code_request = requests.get(url=zip_code_URL)

#     # extracting data in json format
#     zip_code_json_data = zip_code_request.json()
#     # received latitude coordinates
#     zip_latitude = zip_code_json_data["lat"]
#     # received longitude coordinates
#     zip_longitude = zip_code_json_data["lng"]
#     return zip_latitude, zip_longitude


# def get_vaccinefinder_data(zipcode_string):
#     """Gets vaccinefinder.org data and writes to vaccineFinderData.csv"""
#     # gets lat/long from zip code
#     latitude, longitude = get_lat_long(zipcode_string)
#     # we are the Postman
#     headers_list = {"User-Agent": 'PostmanRuntime/7.26.10'}
#     # api endpoint url
#     castlight_url = "https://api.us.castlighthealth.com/vaccine-finder/v1/provider-locations/search"
#     # query parameters, search radius can be changed
#     parameters = {
#         "medicationGuids": "779bfe52-0dd8-4023-a183-457eb100fccc,a84fb9ed-deb4-461c-b785-e17c782ef88b,784db609-dc1f-45a5-bad6-8db02e79d44f",
#         "lat": latitude,
#         "long": longitude,
#         "radius": 10}

#     # send api request
#     castlight_api_data = requests.get(url=castlight_url, params=parameters, headers=headers_list, timeout=30)
#     castlight_json_data = castlight_api_data.json()
#     # print(json.dumps(castlight_json_data, indent=4, sort_keys=True))

#     # get the providers list of dictionaries and sort (thanks Ron for help with previous example)
#     castlight_providers = json.dumps(castlight_json_data['providers'], indent=4, sort_keys=True)
#     # convert to string
#     castlight_loads = json.loads(castlight_providers)
#     # drop these columns
#     columns_to_drop = ["address2", "guid", "phone", "lat", "long", "distance"]
#     # flatten
#     normalized_data = pandas.json_normalize(castlight_loads)
#     # drop columns
#     normalized_data.drop(columns=columns_to_drop, inplace=True)
#     # write to csv
#     normalized_data.to_csv('vaccineFinderData.csv')

