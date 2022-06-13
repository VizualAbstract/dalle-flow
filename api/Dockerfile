FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Install pip
RUN apt-get update && apt-get install -y python3-pip

# Istall git
RUN apt-get install -y git

# Update pip
RUN pip3 install --upgrade pip

# Add requirements
COPY ./requirements.txt /app/requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Add source code
COPY . /app

# Expose
EXPOSE 8080

# Run server
CMD python3 app.py 8080
