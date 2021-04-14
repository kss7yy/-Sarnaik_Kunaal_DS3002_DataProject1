FROM python:3

COPY sarnaik_bot.py sarnaik_bot.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./sarnaik_bot.py"]