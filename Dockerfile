# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /apps
WORKDIR /apps

# Copy the current directory contents into the container at /app
COPY . /apps

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
