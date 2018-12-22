FROM python:3.6
RUN apt-get update
RUN apt-get install python3-pip -y
ADD . /website
WORKDIR /website
RUN pip install --no-cache-dir -r requirements.txt
RUN gunicorn app:app -b 0.0.0.0:5000 --workers-4 --log-level=warning