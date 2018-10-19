FROM python:3.7.0-alpine3.8

COPY version-app.py ./app.py

RUN pip install flask gunicorn


CMD ["gunicorn", "--log-level=info", "--timeout=260", "--bind", "0.0.0.0:5000", "app:app"]

