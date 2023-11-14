FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y libpcap0.8


COPY . .

CMD [ "python", "./network_scanner.py" ]

