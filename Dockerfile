# Install required packages
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Install pytest and coverage tool for HTML report generation
RUN pip install pytest pytest-cov


# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
