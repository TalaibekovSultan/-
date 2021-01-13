json_filename = 'data.json'
from ramashka import romoshko
romoshko()
with open(json_filename, 'r') as f:
    file_content = f.read()
    saved_dict = json.loads(file_content)