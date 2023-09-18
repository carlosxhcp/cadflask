# Base Image
FROM python:3.9-slim

# Work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy other project files
COPY . /app/

# Expose a port to Containers 
EXPOSE 5000

# Command to run on server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]