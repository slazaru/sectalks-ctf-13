FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements2.txt /app2/requirements2.txt

WORKDIR /app2

RUN pip install -r requirements2.txt

COPY app2.py /app2

ENTRYPOINT [ "python3" ]

CMD [ "app2.py" ]

