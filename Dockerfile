# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the directory contents into the container at /src
COPY src/ ./
COPY requirements.txt .

# Copy the SSL certificates into the certs directory at the root level of the container
COPY certs/ /certs/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available (as your Flask app is set to run on this port)
EXPOSE 5000

# Define environment variable
ENV NAME World

# Command to run the application, ensure app.py runs on port 5000 and accessible on all network interfaces
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]
