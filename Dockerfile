FROM python:3.9-slim

# Working directory
WORKDIR /src

# Copy the directory contents into the container at /src
COPY src/ .
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available
EXPOSE 80

# Define environment variable
ENV NAME World

# Command to run the application
CMD ["python", "app.py"]