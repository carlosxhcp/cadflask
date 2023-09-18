
# Base Image
# Fixed typo in base image by changing 'python:FROM3-s.9lim' to 'python:3.9-slim'
FROM python:3.9-slim

# Work directory
# No changes needed
WORKDIR /app

# Copy and install dependencies
# Fixed typo 'requirements' to 'requirements.txt'
COPY requirements.txt requirements.txt

# Install dependencies from requirements.txt
# No changes needed
RUN pip install --no-cache-dir -r requirements.txt

# Copy other project files
# No changes needed
COPY . .

# Expose a port to Containers
# Removed duplicate 'EXPOSE' command, assuming the first port (8080) is to be used
EXPOSE 8080

# Command to run on server
# No changes needed
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
