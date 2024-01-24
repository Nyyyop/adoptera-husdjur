from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return """
  <h1>Adopt a Pet!</h1>
  <p>Browse thru da links below 2 find ur new furry friend: (3) </p>
  <ul>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  """


@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>List of {pet_type}</h1><ul>"
  for pet in pets[pet_type]:
    html += f"<li>{pet['name']}</li></ul>"
  return html 

@app.route('/animals/<pet_type>/<pet_id>')
def pet(pet_type, pet_id):
  pet = 
  

# Viktigt: Denna kodrad ska alltid placeras längst ner i filen.
# Detta för att säkerställa en korrekt uppstart av servern.
app.run(debug=True, host="0.0.0.0")
