# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
COPY templates templates

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 8080

# Define the command to run the Flask application
CMD ["python", "app.py"]
