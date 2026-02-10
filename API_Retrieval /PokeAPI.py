import  requests

base="https://pokeapi.co/api/v2/"
name=input("Enter your Pokemon name: ").lower()


def Get_Pokemon(name):
    url = base+"pokemon/"+name
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        return pokemon
    else:
        print("Pokemon not found",{response.status_code})

poke=Get_Pokemon(name)
if poke:
    print("--------------Pokemon Details---------------")
    print(f"Name : {poke['name'].capitalize()}")
    print(f"Pokemon height : {poke['height']}")
    print(f"Pokemon weight : {poke['weight']}")

    print("Pokemon id :",{poke['id']})

    for ability in poke["abilities"]:
        print(ability["ability"]["name"])


