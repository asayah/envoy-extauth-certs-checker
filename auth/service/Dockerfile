FROM python:3-alpine
RUN apk add gcc
RUN apk add musl-dev libffi-dev linux-headers

RUN pip3 install -q Flask==2.0.3
RUN pip3 install -q cryptography
RUN pip3 install -q urllib3
COPY . ./app
CMD ["python3","-u", "/app/service/server.py"]
