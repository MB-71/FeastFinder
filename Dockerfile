# Using alpine as a base:
FROM python:3.12.2-alpine

# Maintainer information
LABEL maintainer="Michael Brewer <brewer7@pdx.edu"

# Copy contents of current to app
COPY . /app

# Set working directory
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN pip install --no-cache -r requirements.txt

# Set the parameters to the program
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app