import requests

url = "http://portal.apps.noiseaware.io/thresholds/list"

payload = {
    "filter": [
        {
            "key": "property",
            "operator": ">",
            "value": "4"
        }

    ],
    "pagination": {
        "pageNum": 2,
        "perPage": 10
    },
    "search": "112342",
    "sort": [
        {
            "key": "created_at",
            "order": "ASC"
        }
    ]
}
headers = {
    "accept": "application/vnd.threshold.list.response+json",
    "content-type": "application/json",
    "Authorization": "your_token_here" # Make sure to replace with auth token
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)