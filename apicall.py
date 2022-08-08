import requests

my_request = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = my_request.json()

print(json_data.keys())
# print(json_data['abilities'])
# print(json_data['sprites'].keys())
# print(json_data['sprites']['front_default'])

print(json_data['id'])
print(json_data['name'])
print(json_data['abilities'][0]['ability']['name'])
print(json_data['abilities'][1]['ability']['name'])
print(json_data['stats'][0]['stat']['name'])
print(json_data['stats'][0]['base_stat'])
print(json_data['stats'][1]['stat']['name'])
print(json_data['stats'][1]['base_stat'])
print(json_data['stats'][2]['stat']['name'])
print(json_data['stats'][2]['base_stat'])
print(json_data['weight'])
print(json_data['types'][0]['type']['name'])