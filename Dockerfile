FROM python:3.8-alpine

COPY version-app.py ./app.py

RUN pip install pipenv && pipenv install


CMD ["pipenv", "run", "gunicorn", "--log-level=info", "--timeout=260", "--bind", "0.0.0.0:5000", "app:app"]

