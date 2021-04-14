# Builds the Dockerfile from the python3 basic container.
FROM python:3

# Copies over the sarnaik_bot.py script and requirements.txt file
#  sarnaik_bot.py script contains the executable information
#  requirements.txt text file contains the necessary libraries for the python script to execute successfully.
COPY sarnaik_bot.py sarnaik_bot.py
COPY requirements.txt requirements.txt

# RUN command to have pip (python's installer) to install the libraries in requirements.txt
RUN pip install -r requirements.txt

# ENTRYPOINT command to have default docker run statement execute 'python sarnaik_bot.py'
ENTRYPOINT ["python", "./sarnaik_bot.py"]

# Reminder for reader, proper usability of the application is as follows:
#  docker run -e KEY="<Discord channel key>" kss7yy/sarnaik_pokedex "<Pokémon name>"