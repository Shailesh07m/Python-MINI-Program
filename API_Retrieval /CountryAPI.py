# Import requests library
# This library allows us to send HTTP requests to APIs
import requests


# Define function to fetch country data
def get_country(country_name):

    # Construct API URL
    # ?fullText=true ensures exact country name match
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"

    try:
        # Send GET request with timeout
        # timeout=5 means: wait maximum 5 seconds
        response = requests.get(url, timeout=5)

        # If status code is 4xx or 5xx, this will raise an HTTPError
        response.raise_for_status()

        # Convert JSON response into Python object
        # REST Countries returns a LIST of country objects
        return response.json()

    # This runs if country does not exist (404 error)
    except requests.exceptions.HTTPError:
        print("Country not found.")

    # This runs if:
    # - Internet connection fails
    # - Server unreachable
    # - Request times out
    except requests.exceptions.RequestException:
        print("Network error occurred.")

    # If any error happens, return None
    return None


# Take user input
# .strip() removes extra spaces
country = input("Enter your country: ").strip()

# Call function
data = get_country(country)


# Check if data was returned successfully
if data:

    # API returns a list → take first element
    country_info = data[0]

    print("\n----- Country Details -----")

    # ---------------- Name ----------------

    # Safely access nested dictionary using .get()
    # .get() prevents KeyError if key missing
    name_info = country_info.get("name", {})
    official_name = name_info.get("official", "N/A")

    print("Official Name:", official_name)


    # ---------------- Capital ----------------

    # Capital is usually a list
    capitals = country_info.get("capital")

    if capitals:
        # Join multiple capitals if present
        print("Capital:", ", ".join(capitals))
    else:
        print("Capital: Not Available")


    # ---------------- Population ----------------

    population = country_info.get("population", "N/A")
    print("Population:", population)


    # ---------------- Languages ----------------

    print("\nLanguages Spoken:")

    languages = country_info.get("languages")

    if languages:
        # languages is a dictionary → get values
        for language in languages.values():
            print("-", language)
    else:
        print("No language data available.")


    # ---------------- Currencies ----------------

    print("\nCurrencies:")

    currencies = country_info.get("currencies")

    if currencies:
        # currencies is dictionary
        # .items() returns (key, value)
        for code, details in currencies.items():

            currency_name = details.get("name", "N/A")
            currency_symbol = details.get("symbol", "N/A")

            print("Currency Code:", code)
            print("Currency Name:", currency_name)
            print("Currency Symbol:", currency_symbol)
            print()
    else:
        print("No currency data available.")


else:
    print("No data received.")
