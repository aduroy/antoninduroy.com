FROM python:3.10

WORKDIR /code

EXPOSE 8080

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "main.py"]