#!/usr/bin/env python3

'''
Name: Kunaal Sarnaik (kss7yy@virginia.edu)
Course: DS 3002 - Data Science Systems (Spring 2021)
Date: April 14th, 2021
Professor: Neal Magee, Ph.D.
Project Name: The Pokedex
Assignment: DS3002 Data Project #1

Github Repository: https://github.com/kss7yy/-Sarnaik_Kunaal_DS3002_DataProject1
Docker Container: https://hub.docker.com/repository/docker/kss7yy/sarnaik_pokedex
API Source: https://pokeapi.co/
'''

# Import statements for relevant Python libraries/modules
import json
import requests
import sys
import os

if len(sys.argv) < 2:
    sys.exit("\nERROR! No command line arguments were inputted into the \'docker run\' command (excluding the executable file). The usability of this application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")
if len(sys.argv) > 2:
    sys.exit("\nERROR! Extraneous command line arguments were inputted into the \'docker run\' command. The usability of this application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")

poke_api_url = "https://pokeapi.co/api/v2/pokemon/"
poke_api_url_with_param = poke_api_url + (sys.argv[1].lower())

response = requests.get(poke_api_url_with_param)

if response.status_code == 404:
    sys.exit("\nERROR! The Pokémon that you entered as a parameter was not found in the Pokédex! This is either because the Pokémon you entered does not exist, or the Pokémon's name was spelled incorrectly. Please check for these possible sources of error in your command line input.\n\nFor a list of possible Pokémon, click the following link: https://www.pokemon.com/us/pokedex/ \n\nAs a reminder, the proper usability of this application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")

data = json.loads(response.text)

new_line = "\n\n"
def info_formatter(s, length):
    s = s.rstrip(',')
    s = s.lstrip()
    if length > 1:
        last_comma = s.rindex(',', 0, len(s))
        s = s[:last_comma] + " and" + s[last_comma+1:]
    return s

name = data['name'].capitalize()
height = data['height']
weight = data['weight']

moves = data['moves']
moves_string = ""
for move in moves:
    moves_string = moves_string + " " + move['move']['name'] + ","
moves_string = info_formatter(moves_string, len(moves))

abilities = data['abilities']
abilities_string = ""
for ability in abilities:
    abilities_string = abilities_string + " " + ability['ability']['name'] + ","
abilities_string = info_formatter(abilities_string, len(abilities))

pic_url = data['sprites']['front_default']

content = name + " is a Pokémon possessing a height of " + str(height) + " decimeters and weighing " + str(weight) + " hectograms." + new_line
content = content + name + " can be trained to possess any of the following move(s): " + moves_string + "." + new_line
content = content + "One may find " + name + " possessing any of the following ability(ies): " + abilities_string + "." + new_line
content = content + "Here is a picture of " + name + ":\n" + pic_url
print(content)

data = { 
    "content": content,
    "username": "Pokédex",
    "avatar_url": "https://articles.pokebattler.com/wp-content/uploads/2018/08/pokedex-kanto-1.jpg"
}

url = os.environ['KEY']

try:
    response = requests.post(url, json = data)
except Exception as e:
    print("\nThe post to the Discord channel was unsuccessful. Please check the sensitive key you passed into the 'docker run' command. The proper usability of the application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")
    SystemExit(e)