# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the directory contents into the container at /src
COPY src/ ./
COPY requirements.txt .
COPY certs/ /certs/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available
EXPOSE 5000

# Define environment variable
ENV NAME World

# Command to run the application using Gunicorn
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5000", "app:app", "--certfile=/certs/cert.pem", "--keyfile=/certs/key.pem"]
