ARG BUILD_ENV=release # or dev

FROM python:3.9-slim AS build_release

# Set the working directory in the container
WORKDIR /src

# Copy the directory contents into the container at /src
COPY src/ ./
COPY requirements.txt .

# Copy the data directory into the container at the correct path
COPY data/ /data/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available
EXPOSE 5000

# Define environment variable
ENV NAME World

# Add version label
LABEL version="0.1.0"

# Command to run the application using Gunicorn (without certs)
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5000", "app:app"]


FROM build_release AS build_dev

# Copy certificates
COPY certs/ /certs/

# Command to run the application using Gunicorn with certs
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5000", "app:app", "--certfile=/certs/cert.pem", "--keyfile=/certs/key.pem"]


# Create final image (build_dev or build_release)
FROM build_$BUILD_ENV