import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("JSEARCH_API_KEY")

def fetch_jobs(title="software engineer", location="new york"):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": f"{title} in {location}",
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("Error:", response.status_code, response.text)
        return []
