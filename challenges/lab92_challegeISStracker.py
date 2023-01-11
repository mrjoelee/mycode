#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com
Challenge 92: ISS Tracker
"""

import requests
import time
import datetime
import reverse_geocoder as rg

def main():
    """runtime"""

    #part 1 - using requests, access the API
    API = "http://api.open-notify.org/iss-now.json"

    response = requests.get(API)
    iss_data = response.json()

    print(iss_data)

    #part 2 - get data like this:
    """
    CURRENT LOCATION OF THE ISS:
    Lon: -52.7658
    Lat: 37.1268
    """
    lat = iss_data['iss_position']['longitude']
    lon = iss_data['iss_position']['latitude']

    #part 4 - using geocoder to get the location human readable
    # reverse_geocoder must be passed a tuple as the argument
    coords_tuple = (lat, lon)
    result = rg.search(coords_tuple, verbose=False) #verbose=False removes an annoying output that reads - "loading formatted geocded file..."
    #print(result)

    #storing city and country
    city = result[0]['name']
    country = result[0]['cc']

    # part3 : super bonus, print Eoch time works
    epoch_time = int(time.time())
    date_time = datetime.datetime.fromtimestamp(epoch_time)
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {date_time}")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    print(f"City/Country: {city}, {country}")


if __name__ == "__main__":
    main()
