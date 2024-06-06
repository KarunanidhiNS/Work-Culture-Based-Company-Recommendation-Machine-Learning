# Use an existing Docker image as a base
FROM python:3.7

# Set the working directory in the container
WORKDIR /Work_Culture

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ .

# Command to run your application
CMD ["python", "Work_Culture.py"]
