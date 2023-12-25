FROM python:3.11.5-slim-bullseye

WORKDIR /myapp

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /myapp

#ENV FLASK_APP=myapp

CMD flask --app myapp run -h 0.0.0.0 -p $PORT