# This file is used to get flight data from the public API and output the information in json file format which are to
# be used in other modules of this project

import json
import requests
import time


def loadFlightData():
    # API endpoint URL
    url = "https://api.adsb.lol/v2/ladd"

    # Response from server
    response = requests.get(url)

    # Check if HTTP response is 200(Successful)
    if response.status_code == 200:

        # Convert data to json format
        data = response.json()

        # Dumps data to json file
        with open('flight_data.json', 'w') as flight_data:
            json.dump(data, flight_data, indent=4)
            time.sleep(3)
        return True

    else:
        print("There was an error while fetching data")
        return False
