import requests

def get_wether():
    url="https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            da=response.json()
            return da
        else:
            print("No data found",response.status_code)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error:{err.response.status_code}")
    except requests.exceptions.ConnectionError as err:
        print(f"Connection Error:{err.response.status_code}")
    except requests.exceptions.Timeout as err:
        print(f"Timeout Error:{err.response.status_code}")
        return None

data = get_wether()

if data:
    print(data["current_weather"]["temperature"])
    print(data["current_weather"]["windspeed"])
    print(data["current_weather"]["winddirection"])

    if data["current_weather"]["is_day"]==1:
        print("Its a day")
    else:
        print("Its a night")
