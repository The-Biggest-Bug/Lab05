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
        with open("GEO.json", 'r') as f:
            geo = json.load(f)
        for item in geo:
            gstID = item.get("gstID")
            startTime = item.get("startTime")
            allkpIndex = item.get("allKpIndex")
            event = item.get("linkedEvents")
            submission_time = item.get("submissionTime")
            versionID = item.get("versionID")
            notif = item.get("sentNotifications")

        print("                 GEO DATA")
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
    try:
        with open("CME.json", 'r') as f:
            data = json.load(f)
        for item in data:
            flrItem = item.get("flrID")
            catalog = item.get("catalog")
            instruments = item.get("instruments")
            beginTime = item.get("beginTime")
            peakTime = item.get("peakTime")
            endTime = item.get("endTime")
            classType = item.get("classType")
            sourceLocation = item.get("sourceLocation")
            activeRegionNum = item.get("activeRegionNum")
            note = item.get("note")
            submissionTime = item.get("submissionTime")
            versionId = item.get("versionId")
            link = item.get("link")
            linkedEvents = item.get("linkedEvents")
            sentNotifications = item.get("sentNotifications")

        print("             SOLAR FLARE DATA")
        print("============================================\n")
        print(f"Flare Item: {flrItem}")
        print(f"Catalog: {catalog}")
        print(f"Instruments (display name): {instruments}")
        print(f"Flare Begin Time: {beginTime}")
        print(f"Peak Flare Time: {peakTime}")
        print(f"Flare End Time: {endTime}")
        print(f"Class Type: {classType}")
        print(f"Source Loaction: {sourceLocation}")
        print(f"Active Region: {activeRegionNum}")
        print(f"Note: {note}")
        print(f"Submission Time: {submissionTime}")
        print(f"Version ID: {versionId}")
        print(f"Link: {link}")
        print(f"Linked Events: {linkedEvents}")
        print(f"Sent Notifications: {sentNotifications}\n")

    except requests.RequestException as e:
        print(f"Problem fetching Solar Flare data: {e}")
        

def main():
    print("================================================")
    print("|             Main API Option Menu             |")
    print("================================================")
    print("|                 Description:                 |")
    print("| These chosen API's are composed of info ste- |")
    print("| ming from astronomical data provided by NASA |")
    print("| instruments. There are 3 different API's to  |")
    print("| choose from: Coronal Mass Ejection, Geomagn- |")
    print("| etic Storm, or Solar Flare. Choose between a |")
    print("| selection: 1, 2, or 3 to procede to data.    |")
    print("================================================")
    print("| 1) Coronal Mass Ejection Study               |")
    print("| 2) Geomagnetic Storm Study                   |")
    print("| 3) Solar Flare Study                         |")
    print("================================================")
    user_choice = input("             Choose your study: ")
    print("\n\n")

    if user_choice == "1":
        get_all_cleaned_CME_data()
    elif user_choice == "2":
        get_geo_storm()
    elif user_choice == "3":
        get_solar_flare()
    else:
        print("Invalid User Input")

    

if __name__ == "__main__":
    main()
    


