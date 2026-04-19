FROM python:3.11-alpine

COPY ./src/requirements.txt /tmp/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /tmp/requirements.txt

COPY ./src /app

WORKDIR /app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
