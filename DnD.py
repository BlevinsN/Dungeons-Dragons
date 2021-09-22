import requests
from Dnd_Structures import *
from Dnd_Functions import *

r = requests.get('https://www.dnd5eapi.co/api/spells/acid-arrow/')
new_object = add_object(r.json())
print(new_object.name)