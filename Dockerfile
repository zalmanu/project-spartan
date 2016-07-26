FROM python:2.7
ADD requirements.txt /project-spartan/
WORKDIR /project-spartan/
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' myuser
