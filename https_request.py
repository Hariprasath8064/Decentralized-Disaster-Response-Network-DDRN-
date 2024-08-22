import requests

def fetch_geospatial_data(location):
    url = f"https://api.example.com/geospatial?location={location}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Geospatial data for {location}: {response.json()}")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    location = input("Enter location: ")
    fetch_geospatial_data(location)
