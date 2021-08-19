FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python-dev librocksdb-dev build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev liblz4-dev
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD [ "bash", "/app/entrypoint.sh" ]