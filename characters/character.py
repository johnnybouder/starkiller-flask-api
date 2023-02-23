

from db import get_db

def get_characters():
    return get_db()

def get_character(id):
    characters = get_db()
    for character in characters:
        if character["id"] == int(id):
           return character
        
    return 'No character found'