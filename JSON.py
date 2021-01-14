import json

json_filename = 'data.json'

from ramashka import complex_dict

with open(json_filename, 'w') as file:
    json.dump(complex_dict, file)
