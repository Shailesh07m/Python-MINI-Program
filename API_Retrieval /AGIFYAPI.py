import requests


def get_age(*args):
    url= f"https://api.agify.io/?name[]={args[0]}&name[]={args[1]}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout as err:
        print(f"Timeout Error:{err.response.status_code}")
    except requests.exceptions.HTTPError as err:
        print(f"Connection Error:{err.response.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Connection Error:{err.response.status_code}")

data=get_age("Uday","Nitin")
if data:
    for person in data:
        print("Name:",person["name"])
        print("Average Age :",person["age"])
        print("Total Person Count :",person["count"])

#chat gpt version

import requests

def get_age(*names):
    url = "https://api.agify.io/"

    # Build query parameters properly
    params = [("name[]", name) for name in names]

    try:
        # requests automatically builds the query string
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return None


data = get_age("Uday", "Nitin")

if data:
    for person in data:
        name = person.get("name")
        age = person.get("age")
        count = person.get("count")

        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Count: {count}")
        print()
