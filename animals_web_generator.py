import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r') as handle:
        return json.load(handle)
    
animals_data = load_data('animals_data.json')

'''
Name: American Foxhound
Diet: Omnivore
Location: North-America
Type: Hound


The English Foxhound doesn’t have a type field, and therefore we will not print this field:
...

Name: English Foxhound
Diet: Omnivore
Location: Europe
'''

def print_animals_data(animals_data):
    """
    Print animals data from the JSON file
    if the field is not present in the animal data, this field will not be printed
    """

    for animal in animals_data:
        name = animal.get('name')
        diet = animal.get('characteristics', None).get('diet')
        location = animal.get('locations', None)[0]
        type = animal.get('characteristics', None).get('type')

        fields = [('Name', name), ('Diet', diet), ('Location', location), ('Type', type)]
        for field in fields:
            if field[1] is None:
                continue

            print(f'{field[0]}: {field[1]}')
        print()

print_animals_data(animals_data)
