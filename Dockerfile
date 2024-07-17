# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn and Flask
RUN pip install gunicorn flask

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Remove the default Nginx configuration file
RUN rm /etc/nginx/sites-enabled/default

# Copy the Nginx configuration file to the container
COPY nginx.conf /etc/nginx/conf.d

# Expose the ports the app runs on
EXPOSE 8080

# Run Nginx and Gunicorn using a shell command
CMD ["sh", "-c", "service nginx start && gunicorn -w 4 -b 0.0.0.0:8080 app:app --timeout 120"]
