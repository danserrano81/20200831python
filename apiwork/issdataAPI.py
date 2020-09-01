#!/usr/bin/python3
"""RZFeeser | Alta3 Research
A script to explore looking up data from RESTful APIs using HTTP(s) protocol"""

# this is part of the python std library
import time

# python3 -m pip install requests
import requests


def main():
    """code to lookup an API"""

    # define the API to lookup
    apitolookup = "http://api.open-notify.org/iss-now.json"

    while True:
        # send an HTTP GET to the API
        r = requests.get(apitolookup)

        # get back 200 code, and strip off json attachment
        if r.status_code == 200:
            issdata = r.json()

            # print out entire data blob to screen
            print(issdata)

            # print out JUST the lat
            print(f"Latitude - {issdata.get('iss_position').get('latitude')}")

            # print out JUST the lon
            print(f"Longitude - {issdata.get('iss_position').get('longitude')}")

            # print out JUST the timestamp
            # print(f"Timestamp - {issdata['timestamp']}") <- will throw an ERROR if 'timestamp' does not exist
            print(f"Timestamp - {issdata.get('timestamp')}")  # .get method return None if 'timestamp' does not exist
            # delay execution
            time.sleep(3.14)

        # if a lookup response is a non-200
        else:
            print(f"Sorry a non 200 response was returned. HTTP code returned was {r.status_code}")
            # print("Sorry a non 200 response was returned. HTTP code returned was " + str(r.status_code))
            # print("Sorry a non 200 response was returned. HTTP code returne was", r.status_code)

            # escape the while loop if the response returned for any lookup is a non-200
            break

    # this only runs once the program leaves the while True: loop
    print("Thanks for checking on the ISS!")


if __name__ == "__main__":
    main()
