FROM python:3.12

# set current working dir, we will put requirements.txt and app dir into it
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app