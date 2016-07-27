FROM python:2.7

RUN mkdir /project-spartan/
RUN wget -qO- https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz | tar -zxf - -C /usr/bin \
    && chown root:root /usr/bin/dockerize
WORKDIR /project-spartan/

COPY ./requirements.txt /project-spartan/requirements.txt

RUN pip install -r requirements.txt

VOLUME /project-spartan
