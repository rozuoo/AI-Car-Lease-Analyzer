import requests

def get_vehicle_details(vin):

    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/{vin}?format=json"

    response = requests.get(url)

    data = response.json()

    vehicle = data["Results"][0]

    return {
        "Make": vehicle["Make"],
        "Model": vehicle["Model"],
        "Model_Year": vehicle["ModelYear"],
        "Manufacturer": vehicle["Manufacturer"]
    }