import json
import http.client
from datetime import datetime

def get_user_activity(username : str):
    host = "api.github.com"
    path = f"/users/{username}/events"
    headers = {"User-Agent":"Python CLI Tool"}
    connection = http.client.HTTPSConnection(host)
    connection.request("GET", path, headers=headers)
    response = connection.getresponse()
    print(response.status, response.reason)
    if response.status != 200:
        raise Exception(f"GitHub API error: {response.status} {response.reason}")

    data = response.read().decode('utf-8')
    events = json.loads(data)
    #print(json.dumps(events, indent=2))
    return events

def parse_data(events : list):
    for event in events:
        event_type = event.get("type")
        event_repo = event.get("repo").get("name")
        event_payload = event.get("payload")
        event_created_at = event.get("created_at")

        if event_type == "WatchEvent":
            print(f"Starred {event_repo} at {format_date(event_created_at)}")
        elif event_type == "PushEvent":
            commits_size = event_payload.get("size")
            print(f"Pushed {commits_size} to {event_repo}")
        elif event_type == "ReleaseEvent":
            pass

def format_date(iso_str : str, output_format : str = "%d.%m.%Y %H:%M"):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return dt.strftime(output_format)



