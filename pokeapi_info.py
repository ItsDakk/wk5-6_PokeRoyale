# Read the documentation first!! Always, always, always first!!

def get_pokemon(name):
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if not response.ok:
            return "Invalid Pokemon name"
        data = response.json()
        pokemon_dict = {
            "name": data['name'],
            "bexp" : data['base_experience'],
            "shiny": data['sprites']['front_shiny'],
            "ability": data['abilities'][0]['ability']['name'],
            "hp": data['stats'][0]['base_stat'],
            "attack": data['stats'][1]['base_stat'],
            "defense": data['stats'][0]['base_stat'],
        }
        
        return pokemon_dict
    
ditto = get_pokemon('ditto')
pikachu = get_pokemon('pikachu')
charizard = get_pokemon('charizard')
mewtwo = get_pokemon('mewtwo')
zapdos = get_pokemon('zapdos')
print(pikachu)
print(ditto)
print(charizard)
print(mewtwo)
print(zapdos)

while True:
    atk_points_p = pikachu['attack'] - ditto['defense']
    atk_points_d = ditto['attack'] - pikachu['defense']
    pikachu['hp'] = pikachu['hp'] - atk_points_d
    print(f"Ditto attacked and did {atk_points_d} damage")
    print(f" Pikachu remaining HP: {pikachu['hp']}")
    if pikachu['hp'] <= 0:
        print("Ditto won")
        break
    ditto['hp'] = ditto['hp'] - atk_points_p
    print(f"Pikachu attacked and only did {atk_points_p} damage")
    print(f" Ditto remaining HP is {ditto['hp']}")
    if ditto['hp'] <= 0:
        print("Pikachu Won")
        break