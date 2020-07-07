FROM python:3.6-slim

LABEL name="Sample" version="1.0"

WORKDIR /deploy

COPY requirements.txt /deploy/
COPY sampleapp /deploy/


RUN python -m pip install -r requirements.txt 

CMD ["flask", "run", "--host=0.0.0.0"]
