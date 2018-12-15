FROM python:3.6.3

MAINTAINER camden.b.moore@gmail.com

USER root

WORKDIR /Senior-Project

ADD . /Senior-Project

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
