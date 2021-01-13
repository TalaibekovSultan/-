from ramashka import romoshko

json_filename = 'data.json'
dict_2 = romoshko()

with open(json_filename, 'r') as f:
    file_content = f.read()
    saved_dict = json.loads(file_content)
