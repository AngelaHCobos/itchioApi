import requests

APIKEY = "qajYO5e4OdI1o95E1elfg6C6QvJ4egI6WeZ4QTa6"

def get(endpoint):
    return requests.get('https://itch.io/api/1/' + APIKEY + endpoint)

print(get("/games").text)