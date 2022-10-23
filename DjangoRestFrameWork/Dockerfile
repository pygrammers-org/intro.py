FROM python:3.10-slim

# Working dir
WORKDIR /usr/src/app

# Enviroment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY start.sh .
RUN chmod +x start.sh

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt && pip install gunicorn

# Copy whole soure code 
COPY . .

# Start application
ENTRYPOINT ["bash","start.sh"]