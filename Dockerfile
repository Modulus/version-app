FROM python:3.8-alpine

COPY version-app.py ./app.py
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv && pipenv install && pipenv lock --requirements > requirements.txt && pip install -r requirements.txt


CMD ["gunicorn", "--log-level=info", "--timeout=260", "--bind", "0.0.0.0:5000",  "app:app"]

