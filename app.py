from flask import Flask
from helper import pets
app = Flask(__name__)

@app.route('/')
def index():
  """
  Renders the index page of the Adopt a Pet web application.

  Returns:
    str: The HTML content of the index page.
  """
  return """
  <h1>Adopt a Pet!</h1>
  <p>Browse thru da links below 2 find ur new furry friend:</p>
  <ul>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  """

@app.route('/animals/<pet_type>')
def animals(pet_type):
  """
  Renders a list of animals of the specified pet type.

  Args:
    pet_type (str): The type of pet (e.g., 'dogs', 'cats', 'rabbits').

  Returns:
    str: The HTML content of the animal list page.
  """
  html = f"<h1>List of {pet_type}</h1><ul>"
  for pet in pets[pet_type]:
    html += f'<li><a href="/animals/{pet_type}/{pet["name"]}">{pet["name"]}</li></ul>'
  return html 

@app.route('/animals/<pet_type>/<pet_id>')
def pet(pet_type, pet_id):
  """
  Renders the details of a specific pet.

  Args:
    pet_type (str): The type of pet (e.g., 'dogs', 'cats', 'rabbits').
    pet_id (str): The ID or name of the pet.

  Returns:
    str: The HTML content of the pet details page.

  Raises:
    None

  Examples:
    >>> pet('dogs', 'Buddy')
    "pet type is: dogs.<br> and pet name is: Buddy. <br><img src='https://example.com/dog.jpg'>"

    >>> pet('cats', 'Whiskers')
    "pet type is: cats.<br> and pet name is: Whiskers. <br><img src='https://example.com/cat.jpg'>"
  """
  for pet in pets[pet_type]:
    if pet['name'] == pet_id:
      return f"pet type is: {pet_type}.<br> and pet name is: {pet_id}. <br><img src='{pet['url']}'><br>description: {pet['description']}"
  return "404"


app.run(debug=True, host="0.0.0.0")