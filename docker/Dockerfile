# pull official base image
FROM ubuntu:22.04

# install dependencies
RUN apt update && apt install libpq-dev python3 python3-pip -y
RUN pip install -U poetry
COPY . . 
RUN poetry install

# run entrypoint.prod.sh
ENTRYPOINT ["./entrypoint.sh"]
