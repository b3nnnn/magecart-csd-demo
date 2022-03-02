FROM python:3.8-slim-buster

LABEL org.opencontainers.image.source = "https://github.com/b3nnnn/magecart-csd-demo"
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
