import json

# Read the contents of the json file
with open('voting.json', encoding='utf-8') as file:
  data = json.load(file)
  print(data)
# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in data:
  data[person_name] += 1
else:
  data[person_name] = 1

# Save voting data to json file
with open('voting.json', 'w', encoding='utf-8') as file:
  json_object = json.dumps(data, indent=2)
  file.write(json_object)