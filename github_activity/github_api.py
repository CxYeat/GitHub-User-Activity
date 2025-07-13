import json
import http.client
from datetime import datetime

class GitHubActivity:

    def __init__(self, username : str):
        self.username = username
        self.host = "api.github.com"
        self.headers = {"User-Agent":"Python CLI Tool"}

    def get_user_events(self) -> list:
        connection = http.client.HTTPSConnection(self.host)
        path = f"/users/{self.username}/events"
        connection.request("GET", path, headers=self.headers)
        response = connection.getresponse()
        #print(response.status, response.reason)
        if response.status != 200:
            raise Exception(f"GitHub API error: {response.status} {response.reason}")
        data = response.read().decode('utf-8')
        events = json.loads(data)
        #print(json.dumps(events, indent=2))
        return events

    def parse_data(events : list):
        for idx,event in enumerate(events, start = 1):
            event_type = event.get("type")
            event_repo = event.get("repo").get("name")
            event_payload = event.get("payload")
            event_created_at = event.get("created_at")

            print(f"{idx}. ", end="")

            if event_type == "WatchEvent":
                print(f"Starred {event_repo} at {GitHubActivity.format_date(event_created_at)}")
            elif event_type == "PushEvent":
                commits_size = event_payload.get("size")
                print(f"Pushed {commits_size} to {event_repo} at {GitHubActivity.format_date(event_created_at)}")
            elif event_type == "ReleaseEvent":
                event_name = event_payload.get("release").get("name")
                print(f"Published {event_repo} with the name {event_name} at {GitHubActivity.format_date(event_created_at)}")
            elif event_type == "CreateEvent":
                event_ref = event_payload.get("ref")
                event_ref_type = event_payload.get("ref_type")
                print(f"Created new '{event_ref}' in {event_repo} at {GitHubActivity.format_date(event_created_at)}")
            elif event_type == "PullRequestEvent":
                event_payload_action = event_payload.get("action")
                print(f"Pull request was being {event_payload_action} in {event_repo} at {GitHubActivity.format_date(event_created_at)}")
            else:
                print(f"Unknown event type '{event_type}'")

    @staticmethod
    def format_date(iso_str : str, output_format : str = "%d.%m.%Y %H:%M") -> str:
        try:
            dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
            return dt.strftime(output_format)
        except Exception:
            return iso_str  # fallback if format broken



