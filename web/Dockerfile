FROM python
LABEL org.opencontainers.image.source = "https://github.com/b3nnnn/magecart-csd-demo"
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gunicorn_starter.sh"]
