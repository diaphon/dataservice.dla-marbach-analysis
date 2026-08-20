#!/usr/bin/env python3
import requests, json

BASE_URL = "https://dataservice.dla-marbach.de/v1/records"
params = {
    "q": "collection_id_mv:BF00012005", # A:Eich, Günter (letzte Ziffer von der Mediennr. entfernen)
    "format": "json",
    # "size": "10",
}

response = requests.get(BASE_URL, params=params)
print(response.url)
response.raise_for_status()

data = response.json()

with open("BF000120054.json", 'w') as fh:
    json.dump(data, fh, indent=2)