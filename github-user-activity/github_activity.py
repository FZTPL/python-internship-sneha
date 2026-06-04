import sys #the command line interpreter
import ssl
import certifi
import urllib.request #use to fetch the api requested
import urllib.error #handles error such as no-api
import json #to ocnvert the byte(json date) to python fornmat

# Check if username was provided
if len(sys.argv) < 2:
    print("Usage: python3 github_activity.py <username>")
    sys.exit(1)

username = sys.argv[1] #username is the second argument passed to the script

url = f"https://api.github.com/users/{username}/events" #url created to fetch the public events of the user

try:
   
    context = ssl.create_default_context(cafile=certifi.where())

    response = urllib.request.urlopen(url, context=context)  # Fetch data from GitHub API
    data = response.read()  # Read response bytes
    events = json.loads(data) # Convert JSON to Python objects now in lost format
    if len(events) == 0:
        print("No recent public activity found.")
        sys.exit(0)

    for event in events:
        event_type = event["type"] #we havea directory which return these type of format so
        repo_name = event["repo"]["name"]

        if event_type == "PushEvent":
            commit_count = len(event["payload"].get("commits", [])) #here it returns empty list if it doesnt exist
            print(f"- Pushed {commit_count} commits to {repo_name}")

        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")

        elif event_type == "CreateEvent":
            print(f"- Created in {repo_name}")

        else:
            print(f"- {event_type} in {repo_name}")

except urllib.error.HTTPError as e:
    if e.code == 404:
        print("GitHub user not found.") 
    else:
        print(f"HTTP Error: {e.code}")

except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")

except Exception as e:
    print(f"Error: {e}")