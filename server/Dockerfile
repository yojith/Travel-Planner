# Everytime a change is made, all of these commands need to be run in cmd
# gcloud builds submit --tag gcr.io<project-id>
# gcloud run deploy --image gcr.io<project-id>
# firebase deploy --only hosting

# 1 
FROM python:3.12

# 2

# Copies requirements.txt file from server folder to a newly created forder called tmp and installs the libraries on requirements.txt
# COPY requirements.txt tmp/
# RUN pip install -r /tmp/requirements.txt

# Run this command if not using requirements.txt
RUN pip install Flask gunicorn

# 3
COPY src/ app/
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
