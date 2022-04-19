FROM python:3.8.2-slim

#Update
RUN apt-get update

#Install Requirements
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

#Copy app
COPY . /api
WORKDIR /
EXPOSE 5000
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "-t", "30", "--reload", "api.wsgi:app"]
#CMD ["gunicorn", "-w", "3", "-t", "30", "api.wsgi:app"]

# gunicorn -w 3 -b :5000 -t 30 --reload wsgi:app