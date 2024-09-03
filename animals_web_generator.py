import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, 'r') as handle:
        return json.load(handle)


def print_animals_data(animals_data):
    """
    Print animals data from the JSON file
    if the field is not present in the animal data, this field will not be printed
    """

    output = '<ul class="cards">'

    for animal in animals_data:
        name = animal.get('name')
        diet = animal.get('characteristics', None).get('diet')
        location = animal.get('locations', None)[0]
        type = animal.get('characteristics', None).get('type')

        output += '<li class="cards__item">'    

        fields = [('Name', name), ('Diet', diet), ('Location', location), ('Type', type)]
        for field in fields:
            if field[1] is None:
                continue

            output += (f'{field[0]}: {field[1]}<br/>')

        output += '</li>'
    output += '</ul>'
    return output


def read_html_template(file_path):
    """ Reads HTML template file """
    with open(file_path, 'r') as handle:
        return handle.read()


animals_data = load_data('animals_data.json')
file_path = 'animals_template.html'
template = read_html_template(file_path)
output = print_animals_data(animals_data)
final_template = template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as handle:
    handle.write(final_template)
