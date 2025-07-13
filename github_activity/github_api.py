import json
import http.client

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
    return events
