# Create an image based in the official python image from dockerhub
FROM python:3.9.1-slim-buster

MAINTAINER gorgeonflorian@gmail.com

# Make a directory for our application
WORKDIR /python-test-calculator

# Copy for source code
COPY . /python-test-calculator

# Install dependencies (--no-cache-dir: looks at every line in the directory)
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "./main.py"] # Works for pytest and without anything
ENTRYPOINT [] # The previous line seems to be enough