#!/usr/bin/python3

import requests


def main():

    resp = requests.get("https://api.spacexdata.com/v3/launches/upcoming")

    for mission in resp.json():
        print(mission.get("flight_number"), mission.get("mission_name"), mission.get("launch_date_utc"))
        ls = mission.get("launch_site").get("site_name_long")
        print(f"\tLaunch Site: { ls }\n")
if __name__ == "__main__":
    main()
