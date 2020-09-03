#!/usr/bin/python3

import requests


def main():

    resp = requests.get("https://anapioficeandfire.com/api/houses")

    for name in resp.json():
        print('House: ' + name.get("name") )
        print('\tRegion: ' +  name.get("region") )
        print('\tCoat of Arms: ' + name.get("coatOfArms") + "\n")
        
        if not name.get("overlord"):
            continue
        
        resp = requests.get(name.get("overlord"))
        if resp.status_code == 200:
            resp = resp.json()
            print('\tOverlord: ' + resp.get('name'))

if __name__ == "__main__":
    main()
