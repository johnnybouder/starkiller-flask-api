from flask import Flask

from characters.character import get_character, get_characters  

app = Flask(__name__)

# defining a route
@app.route("/") # decorator
def home(): # route handler function
    # returning a response
    return "Hello World!"

@app.route("/api/characters")
def get_characters_view():
    return get_characters()

@app.route("/api/characters/<character_id>")
def get_character_view(character_id: int):
    return get_character(character_id)