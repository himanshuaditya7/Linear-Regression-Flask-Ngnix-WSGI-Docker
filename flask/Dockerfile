FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# run the command to start uWSGI
CMD ["uwsgi", "api.ini"]