FROM python:3.10.0a3-buster

WORKDIR /opt/pihome

RUN apt update && apt install -y nmap
COPY ["./application/", "./"]
RUN pip3 install -r requirements.txt

CMD python3 webapp.py
