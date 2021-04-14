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
import json         # Encoding and decoding JSON data from the API
import requests     # Perform HTTP requests to retrieve JSON data from the API
import sys          # Obtain command line arguments of the parameter (Pokémon name)
import os           # Extracts environment variable (sensitive Discord channel key passed in)

# Command Line Error Handling
#   Using sys.argv (list of command-line arguments), checks if the number of arguments provided were not equal to 2. If less than two, informs the user that they did not input any additional command-line arguments and reminds usability of the application. Then exits using sys.exit(). If greater than 2, informs the user that they inputted extraneous command-line arguments and reminds them of the usability of the application. Then exits using sys.exit() similarly.
if len(sys.argv) < 2:
    sys.exit("\nERROR! No command line arguments were inputted into the \'docker run\' command (excluding the executable file). The usability of this application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")
if len(sys.argv) > 2:
    sys.exit("\nERROR! Extraneous command line arguments were inputted into the \'docker run\' command. The usability of this application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")

# Setting up the url of the PokéAPI for establishing HTTP requests. Establishes the base URL and then appends the command-line parameter to the end of it to retrieve data pertaining to the prompted Pokémon.
poke_api_url = "https://pokeapi.co/api/v2/pokemon/"
poke_api_url_with_param = poke_api_url + (sys.argv[1].lower())

# Retrieves data pertaining to the Pokémon name parameter passed in from the PokéAPI publicly-accessible API. Uses the requests.get() method to do so.
response = requests.get(poke_api_url_with_param)

# Error handling for Pokémons that were not found, either due to mispelling or due to the lack of an existing Pokémon. Informs the user of the possible mispelling or lack of existing Pokémon with the name they entered. Reminds the user of the proper usability of the application and then exits the system using sys.exit() method.
if response.status_code == 404:
    sys.exit("\nERROR! The Pokémon that you entered as a parameter was not found in the Pokédex! This is either because the Pokémon you entered does not exist, or the Pokémon's name was spelled incorrectly. Please check for these possible sources of error in your command line input.\n\nFor a list of possible Pokémon, click the following link: https://www.pokemon.com/us/pokedex/ \n\nAs a reminder, the proper usability of this application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")

# Decodes the JSON data retrieved from PokéAPI regarding the Pokémon the user entered using json.loads() method.
data = json.loads(response.text)

# String to create a double new line when it is needed in the content part of the data payload below.
new_line = "\n\n"

# info_formatter method to format the JSON data retrieved from dictionary to string with 'and' placed in.
#   s - the dictionary that needs to be turned into a string
#   length - length of the dictionary passed in from the JSON data
#   Method strips the last comma and leading space. If the length of the dictionary is more than one, and 'and' is placed in and the last comma is stripped. Otherwise, the string is unchanged after the trailing comma and leading space is stripped.
def info_formatter(s, length):
    s = s.rstrip(',')
    s = s.lstrip()
    if length > 1:
        last_comma = s.rindex(',', 0, len(s))
        s = s[:last_comma] + " and" + s[last_comma+1:]
    return s

# Retreives the name, height, and weight of the Pokémon, capitalizing the name for string readability when placed into the data payload below.
name = data['name'].capitalize()
height = data['height']
weight = data['weight']

# Retreives the moves of the Pokémon. Turns the moves into a string-readable format and uses the info_formatter() method to format it in a readable format for the data payload in a user-friendly manner.
moves = data['moves']
moves_string = ""
for move in moves:
    moves_string = moves_string + " " + move['move']['name'] + ","
moves_string = info_formatter(moves_string, len(moves))

# Retreives the abilities of the Pokémon. Turns the abilities into a string-readable format and uses the info_formatter() method to format it in a readable format for the data payload in a user-friendly manner.
abilities = data['abilities']
abilities_string = ""
for ability in abilities:
    abilities_string = abilities_string + " " + ability['ability']['name'] + ","
abilities_string = info_formatter(abilities_string, len(abilities))

# Retrieves a picture of the Pokémon using PokéAPI's Github repository. The URL embedded in the JSON data directs the user to the image in the repository. The image is a front view of the Pokémon in battle.
pic_url = data['sprites']['front_default']

# Formats the name, height, weight, moves, abilities, and picture of the Pokémon into a human-readable format to be inserted into the data payload. Prints this out to the console so the user can read it even if they do not have the Discord key necessary below.
content = name + " is a Pokémon possessing a height of " + str(height) + " decimeters and weighing " + str(weight) + " hectograms." + new_line
content = content + name + " can be trained to possess any of the following move(s): " + moves_string + "." + new_line
content = content + "One may find " + name + " possessing any of the following ability(ies): " + abilities_string + "." + new_line
content = content + "Here is a picture of " + name + ":\n" + pic_url
print(content)

# Creates the data payload necessary to be POSTed into the Discord channel. Content is the string that was formatted above with information regarding the Pokémon. username is 'Pokédex', and this shows up as the Discord bot's username. avatar_url is a picture of a Pokédex, and this shows up as the avatar of the Discord bot in the channel when the data payload is POSTed.
data = { 
    "content": content,
    "username": "Pokédex",
    "avatar_url": "https://articles.pokebattler.com/wp-content/uploads/2018/08/pokedex-kanto-1.jpg"
}

# Extracts the sensitive Discord Webhook key from the environment. This makes it so that the key, which is considered sensitive information, is not posted in this code and instead passed in to the environment by the user at runtime.
url = os.environ['KEY']

# try-catch statement. Attempts to POST the data payload to the Discord channel. If this does not work, at catch-all Exception is used to inform the user that the correct sensitive key was not inputted. Reminds the user of the proper usability of the application and then exits using SystemExit().
try:
    response = requests.post(url, json = data)
except Exception as e:
    print("\nThe post to the Discord channel was unsuccessful. Please check the sensitive key you passed into the 'docker run' command. The proper usability of the application is as follows:\n\ndocker run -e KEY=\"<discord channel integration key>\" kss7yy/sarnaik_pokedex \"<Pokémon name>\"\n\nPlease see the README.md file in the github repository for this project for more details on usability. Exiting...")
    SystemExit(e)