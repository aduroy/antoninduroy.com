FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

CMD exec gunicorn --bind :$PORT --log-level info --workers 1 --threads 8 --timeout 0 app.main:server