# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY prerequisites.txt .
RUN pip install --upgrade pip && pip install -r prerequisites.txt

# Upgrade Packages
RUN pip install pandas --upgrade
RUN pip install numpy --upgrade

# Copy the application code
COPY . .

# Expose the port used by the OPC UA server simulator
EXPOSE 4840

# Run the command to start the OPC UA server simulator when the container launches
CMD ["python", "opc_ua_server_simulator.py"]
