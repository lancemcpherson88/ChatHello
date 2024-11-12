# Use a minimal Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY app.py .

# Expose port 8080 to match the port that the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]