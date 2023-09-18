
# Base Image

FROM python:3.9-slim

# Work directory

WORKDIR /app

# Copy and install dependencies
# Fixed typo 'requirements' to 'requirements.txt'

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy other project files

COPY . .

# Expose a port to Containers
# Removed the duplicate 'EXPOSE' command as it is trying to expose multiple ports.
# Assuming the first port is the one to be used (8080).

# Command to run on server

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
