# Sarnaik_Kunaal_DS3002_DataProject1

*Author*: Kunaal Sarnaik (kss7yy@virginia.edu)<br/>
*Course*: DS 3002 - Data Science Systems (Spring 2021)<br/>
*Date*: April 14th, 2021<br/>
*Professor*: Neal Magee, Ph.D.<br/>
*Project Name*: The Pokédex (Discord Integration)<br/>
*Assignment*: DS 3002 Data Project #1<br/>

Welcome to my DS3002: Data Science Systems Data Project #1 repository!

This repository contains the necessary text files to write a Dockerized Python3 application that can be run interactively, taking a single parameter ("Discord Integration" option). Using the remote, publicly-accessible **PokéAPI** API (https://pokeapi.co/), I created a Docker container with a Python3 script to retrieve remote Pokémon data based on a user CLI parameter entered (Pokémon name) and have the program post the information to a channel in the DS3002 Spring 2021 Discord server.

The container takes a single parameter when run, performing error handling with an informative "help" screen if the wrong number of command line inputs are received. If the parameter is existent, the container attempts to perform a request against the remote API using that parameter, posting the results on the specified Discord server channel using a sensitive key. The sensitive key must be passed into the container when it is run (usability details are provided later in this document). Finally, if the parameter's information retrieval was unsuccessful or the sensitive key entered by the user was incorrect, the application provides another informative help screen.

Please enjoy this project!

- Github Repository: https://github.com/kss7yy/-Sarnaik_Kunaal_DS3002_DataProject1
- Docker Container: https://hub.docker.com/repository/docker/kss7yy/sarnaik_pokedex
- API Source: https://pokeapi.co/

## Usability

### Creating/Pulling the Dockerfile

### Running the Dockerfile

## Files and General Documentation

1. **Dockerfile**

The Dockerfile contains the instructions necessary to build the Dockerfile. The container is initially built from the Python 3 basic image; this is essentially used as the launching pad for the additions I will make to the image. The first addition includes copying over the *sarnaik_bot.py* script from the directory into the container. The second addition includes copying over the *requirements.txt* file into the container. From there, the RUN command is utilized in order to have pip (Python's installer) install all of the relevant Python libraries that are not already installed with basic Python3. For this application, **requests** is the only library that was necessary to be installed. The last Docker command utilized was the **ENTRYPOINT** line, which specifies the command to be run during all times the Docker container is run. Essentially, this command makes it so that when the usable phrase is called, "python sarnaik_bot.py" will be run in the container, executing the script as planned with command line arguments passed in to the docker run statement.

2. **sarnaik_bot.py**

This script executes the functionality of the application, and in-line comments can also be found from within the executable file. 

First, the relevant modules/libraries, one of which was installed by pip in the Dockerfile (**requests**) are imported into the script: **json**, **requests**, **sys**, and **os**. **json** was imported to encode and decode JSON data, **requests** was imported to perform HTTP requests pertaining to PokéAPI, **sys** was imported to use system-specific parameters and functions (utilized specifically for obtaining the command line argument of the Pokémon name passed in), and **os** was imported to extract the environment variable (Discord channel key) necessary to post the information extracted from PokéAPI into the server.

The script first performs error handling to ensure that the correct number of command line arguments were entered (2, including the executable file in the end). Based on whether the user enters zero or more than 1 additional command line parameter, the error handling stops the script and prints out a informative message using the *sys.exit()* function. If the correct number of command-line parameters was entered (2, including the executable file in the end), the script continues and attempts to retrieve the data relevant to the Pokémon using the **requests** library. However, if the Pokémon is not found (either because user entered name incorrectly or Pokémon does not exist), the script catches the error and outputs an informative error accordingly.

After these initial checks, the script retrieves information regarding the Pokémon name parameter entered and parses the Pokémon's name, height, weight, moves, and abilities, as well as a picture of the Pokémon using PokéAPI. This information is concisely put into a string and printed out to the console to provide successful feedback to the user (see comments for further details regarding the intricacies of the Python code).

Then, the data payload is set up to be POSTed to the relevant channel in the course's discord server. The string outputted to the console is placed into the 'content' value. The 'username' value consists of the Project title - Pokédex. The avatar_url (https://articles.pokebattler.com/wp-content/uploads/2018/08/pokedex-kanto-1.jpg) is a picture of a Pokédex. 

Next, the environmental variable (**KEY**) passed in by the user is extracted from the shell using the **os** library. This key utilizes the "Execute Webhook" method in Discord's API (https://discord.com/developers/docs/resources/webhook#execute-webhook). The key is not published in this repository since it is considered sensitive information. Using the key, the **requests** library is then leveraged to POST the data payload discussed above to the channel. If the post was somehow unsuccessful, a catch-all exception prints out an informative error message and exits the program, likely because the correct key was not passed in. Otherwise, the post is successful and the course's Discord server is able to view what information the user extracted regarding the valid Pokémon.

3. **requirements.txt**

This text file contains the required libraries that must be installed by pip in order for the script to execute successfully. In this case, the **requests** library, used to perform HTTP requests in Python, is the only library/module used by the script that is not already included in default Python3. Thus, the text file only contains **requests** as a string.

## End Notes

This project was programmed through use of Python3, Docker, and Github by Kunaal Sarnaik (kss7yy@virginia.edu). The assignment is Data Project #1 in the DS 3002: Data Science Systems Course at the University of Virginia, taught by professor Neal Magee, Ph.D. during the Spring 2021 semester. DS 3002 was taken for completion of the Data Science Minor at the University of Virginia.