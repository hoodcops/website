FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn wsgi:app -b 0.0.0.0:5000 --workers=4