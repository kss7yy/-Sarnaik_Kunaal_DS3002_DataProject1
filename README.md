# Sarnaik_Kunaal_DS3002_DataProject1

*Author*: Kunaal Sarnaik (kss7yy@virginia.edu)<br/>
*Course*: DS 3002 - Data Science Systems (Spring 2021)<br/>
*Date*: April 14th, 2021<br/>
*Professor*: Neal Magee, Ph.D.<br/>
*Project Name*: The Pokedex (Discord Integration)<br/>
*Assignment*: DS3002 Data Project #1<br/>

Welcome to my DS3002: Data Science Systems Data Project #1 repository!

This repository contains the necessary text files to write a Dockerized Python3 application that can be run interactively, taking a single parameter ("Discord Integration" option). Using the remote, publicly-accessible **PokéAPI** API (https://pokeapi.co/), I created a Docker container with a Python3 script to retrieve remote Pokémon data based on a user CLI parameter entered (Pokémon name) and have the program post the information to a channel in the DS3002 Spring 2021 Discord server.

The container takes a single parameter when run, performing error handling with an informative "help" screen if the wrong number of command line inputs are received. If the parameter is existent, the container attempts to perform a request against the remote API using that parameter, posting the results on the specified Discord server channel using a sensitive key. The sensitive key must be passed into the container when it is run (usability details are provided later in this document). Finally, if the parameter's information retrieval was unsuccessful or the sensitive key entered by the user was incorrect, the application provides another informative help screen.

Please enjoy this project!

- Github Repository: https://github.com/kss7yy/-Sarnaik_Kunaal_DS3002_DataProject1
- Docker Container: https://hub.docker.com/repository/docker/kss7yy/sarnaik_pokedex
- API Source: https://pokeapi.co/

## Files Included

1. **Dockerfile**

The Dockerfile contains the instructions necessary to build the Dockerfile. The container is initially built from the Python 3 basic image; this is essentially used as the launching pad for the additions I will make to the image. The first addition includes copying over the *sarnaik_bot.py* script from the directory into the container. The second addition includes copying over the *requirements.txt* file into the container. From there, the RUN command is utilized in order to have pip (Python's installer) install all of the relevant Python libraries that are not already installed with basic Python3. For this application, **requests** is the only library that was necessary to be installed. The last Docker command utilized was the **ENTRYPOINT** line, which specifies the command to be run during all times the Docker container is run. Essentially, this command makes it so that when the usable phrase is called, "python sarnaik_bot.py" will be run in the container, executing the script as planned with command line arguments passed in to the docker run statement.

2. **sarnaik_bot.py**

This script executes the functionality of the application, and in-line comments can also be found from within the executable file. 
3. **requirements.txt**

## Usability

### Creating/Pulling the Dockerfile

### Running the Dockerfile (USABILITY)

## End Notes

