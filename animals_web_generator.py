import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_html(file_path):
  with open(file_path, "r") as handle:
    return handle.read()


def write_html(file_path, content):
  with open(file_path, "w") as handle:
    handle.write(content)

html_content = read_html("animals_template.html")
animals_data = load_data('animals_data.json')



output = ''
for animal in animals_data:
  output += '<li class="cards__item">\n'
  if "name" in animal:
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
  output += '  <p class="card__text">\n'
  if "diet" in animal["characteristics"]:
    output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
  if "locations" in animal:
    output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
  if "type" in animal["characteristics"]:
    output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
  output += '  </p>\n'
  output += '</li>\n'


final_html = html_content.replace("__REPLACE_ANIMALS_INFO__", output)


write_html("animals.html", final_html)