import json
from urllib import request, response
import requests

"""

Získaná data nějak zpracujte a prohlédněte si je. Vypište, jaké má třetí planeta podnebí a terén. Vypište, jaké kosmické lodě první postava používá.

Zkuste do něj poslat dotaz na třetí planetu vyskytující se ve filmech a pak dotaz na první postavu.
Získaná data nějak zpracujte a prohlédněte si je. Vypište, jaké má třetí planeta podnebí a terén.

"""
#1 task:
# Zkuste do něj poslat dotaz na třetí planetu vyskytující se ve filmech a pak dotaz na první postavu.

base_url = "https://swapi.dev/api/"

planets = base_url + "planets"
heroic = base_url + "people"

url_get = requests.get(base_url)
url_get_planet = requests.get(planets)
url_get_heroic = requests.get(heroic)
#print(url_get.text)
#about_planets = url_get_planet.text
#about_heroics = url_get_heroic.text

jj_planets = url_get_planet.json()
jj_people = url_get_heroic.json()
#print(jj_planets["results"])

#print(jj_planets["results"][2]["name"])
#print(jj_people["results"][3])
# Vypište, jaké má třetí planeta podnebí a terén.
# vyskytující se ve filmech
for planet in jj_planets["results"]:
    if planet == jj_planets["results"][2]:
        print("The third planet is ", planet["name"]) #planet["name"] if deleted a ["name"] you`ll se all information about that planet
        print("This planet was in films :\n",(requests.get((base_url)+(planet["films"][0][22:-1]))).text)
                                            

for men in jj_people["results"]:
    if men == jj_people["results"][0]:
        print(f"The name of first person is - {men['name']}.")
        print("He use this boat :\n",(requests.get((base_url)+(men['vehicles'][0][22:-1])).text))
        print("His second boat is :\n", (requests.get((base_url)+(men['vehicles'][1][22:-1])).text)) 
        # How it work -- first of all i go to the key by value "vehicles", than i go to the first list.
        # and after that i send request , and show it as a text 
