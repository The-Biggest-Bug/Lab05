import requests
import json

CME = "https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY"
GEO_STORM = "https://api.nasa.gov/DONKI/GST?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY"
SOLAR_FLARE = "https://api.nasa.gov/DONKI/FLR?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY"


def get_all_cleaned_CME_data():
    try:
        with open("CME.json", 'r') as f:
            data = json.load(f)
        for item in data:
            activityID = item.get("activityID")
            start_time = item.get("startTime")
            for instrument in item.get('instruments'):
                instrument_1 = instrument["displayName"]
            note = item.get("note")
            for analyses in item.get("cmeAnalyses"):
                cme_1 = analyses["isMostAccurate"]
                cme_2 = analyses["time21_5"]
                cme_3 = analyses["latitude"]
                cme_4 = analyses["longitude"]
                cme_5 = analyses["halfAngle"]
                cme_6 = analyses["speed"]
                cme_7 = analyses["type"]
                cme_8 = analyses["note"]
                cme_9 = analyses["submissionTime"]   
                for list in analyses.get("enlilList"):
                    analyses_1 = list["modelCompletionTime"]
                    analyses_2 = list["au"]
                    analyses_3 = list["isEarthMinorImpact"]
                    analyses_4 = list["cmeIDs"]
                    analyses_5 = list["impactList"]
            
        print("                 CME DATA")
        print("===========================================\n")
        print(f"Activity ID: {activityID}")
        print(f"Start Time: {start_time}")
        print(f"Instruments: {instrument_1}")
        print(f"Note: {note}")
        print(f"CME Analyses - isMostAccurate?: {cme_1}")
        print(f"CME Analyses - Time: {cme_2}")
        print(f"CME Analyses - LAT: {cme_3}")
        print(f"CME Analyses - LONG: {cme_4}")
        print(f"CME Analyses - HalfAngle: {cme_5}")
        print(f"CME Analyses - Speed: {cme_6}")
        print(f"CME Analyses - Type: {cme_7}")
        print(f"CME Analyses - Note: {cme_8}")
        print(f"CME Analyses - Submission Time: {cme_9}")
        print(f"Model Completion Time: {analyses_1}")
        print(f"Astronomical Unit: {analyses_2}")
        print(f"Minor Impact on Earth?: {analyses_3}")
        print(f"CME IDs: {analyses_4}")
        print(f"Impact List: {analyses_5}")

    except requests.RequestException as e:
        print(f"Problem fetching CME data: {e}")


def get_geo_storm():
    try:
        with open("CME.json", 'r') as f:
            geo = json.load(f)
        for item in geo:
            gstID = item.get("gstID")
            startTime = item.get("startTime")
            allkpIndex = item.get("allKpIndex")
            event = item.get("linkedEvents")
            submission_time = item.get("submissionTime")
            versionID = item.get("versionID")
            notif = item.get("sentNotifications")

        print("                 CME DATA")
        print("===========================================\n")
        print(f"gstID: {gstID}")
        print(f"Start Time: {startTime}")
        print(f"All Kp Indeces: {allkpIndex}")
        print(f"Linked Events: {event}")
        print(f"Submission Time: {submission_time}")
        print(f"Version ID: {versionID}")
        print(f"Sent Notifications: {notif}")
            
    except requests.RequestException as e:
        print(f"Problem fetching Geo Storm data: {e}")


def get_solar_flare():
    response = requests.get(SOLAR_FLARE)
    data = response.json()

    filename = "SOLAR.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

get_solar_flare()

'''
response = requests.get(GEO_STORM)
    data = response.json()

    filename = "GEO.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        '''