FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y libpcap0.8

# default docker network
ENV IP_RANGE "172.17.0.0/16"    

COPY . .

CMD [ "python", "./network_scanner.py" ]

