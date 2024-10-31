import requests
import json
import os
from dotenv import load_dotenv

load_dotenv("key.env")

def getMovie(movie):
    movie_api_key = os.getenv("OMDBAPI_API_KEY")
    print(movie, movie_api_key)
    url = f"https://omdbapi.com/?apikey={movie_api_key}&t={movie}"
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print("Useless Fact:", fact_data)
        return fact_data
    else:
        print("Could not get api")
        return None

def europeana_query(query):
    euro_api_key = os.getenv("EUROPEANA_API_KEY")
    url = "https://api.europeana.eu/record/v2/search.json"
    params = {
        'wskey': euro_api_key,
        'query': query,
        'media': 'true',
        'profile': 'rich',
        'rows': 6
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print(f"Europeana API error code: {response.status_code}")
        return []
def main():
    movie = input("Provide a movie name")
    movie_data = getMovie(movie)
    euro_data = europeana_query(movie)
    if not movie_data:
        return

    data_to_save = {
        "movie data": movie_data,
        "euro data": euro_data

    }

    filename = f"MovieData_Europeana.json"
    with open(filename, 'w') as file:
        json.dump(data_to_save, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()

