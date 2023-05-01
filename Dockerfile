# Use an official Python slim runtime based on Alpine as a parent image  
FROM python:3.9-slim  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the src directory contents into the container at /app  
COPY ./src /app
COPY requirements.txt /app
  
# Install any needed packages specified in requirements.txt  
# Adding build dependencies for packages with native extensions  
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
  
# Make port 44480 available to the world outside this container  
EXPOSE 44480

# Run app_streamlit.py with Streamlit when the container launches
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=44480", "--server.address=0.0.0.0"]  