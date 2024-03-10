# This python script contains method that format the data from the json file that contain flight data
# and formats the data so that it is ready to use in other modules

import json
import GetFromAPI

def get_latitudes():
    # Open the json file
    with open('flight_data.json', 'r') as loaded_data:
        # Load the data to a variable
        data = json.load(loaded_data)

    # Get the flights
    aircrafts = data.get("ac", [])
    # Array to hold latitudes
    latitudes = []
    for aircraft in aircrafts:
        lat = aircraft.get("lat", 0)
        latitudes.append(lat)
    return latitudes


def get_longitudes():
    # Open the json file
    with open('flight_data.json', 'r') as loaded_data:
        # Load the data to a variable
        data = json.load(loaded_data)

    # Get the flights
    aircrafts = data.get("ac", [])

    # Array to hold longitudes
    longitudes = []
    for aircraft in aircrafts:
        long = aircraft.get("lon", 0)
        longitudes.append(long)
    return longitudes


def get_aircrafts():
    # Open the json file
    with open('flight_data.json', 'r') as loaded_data:
        # Load the data to a variable
        data = json.load(loaded_data)

    # Get the flights
    aircrafts = data.get("ac", [])

    aircraft_list = []
    for aircraft in aircrafts:
        lat = aircraft.get("lat", 0)
        lon = aircraft.get("lon", 0)

        # Collect data for each plane in a dict object
        aircraft_info = {
            "lat": lat,
            "lon": lon
        }

        # Append each plane's information to list
        aircraft_list.append(aircraft_info)
    return aircraft_list
