import requests

# Replace 6938736476723408000 with activity zone ID
url = "http://portal.apps.noiseaware.io/thresholds/activityZone/6938736476723408000/replace"

payload = { "thresholds": [
        {
            "NRS": 80,
            "TriggerCount": 3,
            "activityZoneID": 6938736476723408000,
            "endTime": 24,
            "startTime": 0,
            "timeZone": "Eastern"
        }
    ] }
headers = {
    "accept": "application/vnd.threshold.replace.response+json",
    "content-type": "application/json",
    "Authorization": "your_token_here" # Make sure to replace with auth token
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)