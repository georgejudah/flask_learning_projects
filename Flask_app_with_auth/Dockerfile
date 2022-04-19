# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

# copy the requirements file into the image
COPY requirements.txt requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]