import requests

r = requests.get('https://www.dnd5eapi.co/api/spells/acid-arrow/')
print(r.text)