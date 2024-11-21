FROM python:3.10

EXPOSE 8000

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["waitress-serve", "--listen=0.0.0.0:8000", "main:server"]