# Create an image based in the official python image from dockerhub
FROM python:3.9.1-slim-buster

MAINTAINER gorgeonflorian@gmail.com

# Make a directory for the application
WORKDIR /python-test-calculator

# Copy the files for source code
COPY . /python-test-calculator

# Install dependencies based on requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT []
# Run the application
CMD ["python", "./main.py"]
