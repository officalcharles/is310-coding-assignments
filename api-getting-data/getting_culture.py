import requests
import json
import os
def get_useless_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print("Useless Fact:", fact_data)
        return fact_data
    else:
        print("Could not get api")
        return None
def main():
    fact_data = get_useless_fact()
    if not fact_data:
        return

    data_to_save = {
        "useless_fact": fact_data["text"]
    }

    filename = f"useless_facts_and_europeana_data.json"
    with open(filename, 'w') as file:
        json.dump(data_to_save, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()

