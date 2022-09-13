import os
from ebird.api import get_nearby_observations
from pprint import pprint

EBIRD_API_KEY = os.environ.get("EBIRD_API_KEY", "")
LON = os.environ.get("LONGITUDE", "")
LAT = os.environ.get("LATITUDE", "")


def main():
    print("main")
    records = get_nearby_observations(EBIRD_API_KEY, LAT, LON, dist=15, back=7)
    # pprint(records)
    common_names = list(set([i["comName"] for i in records]))
    print(common_names)
    

if __name__ == "__main__":
    main()



