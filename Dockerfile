# Use an official Python image as the base
FROM python:3.13.6-slim as builder

# Set the working directory to /app
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential
    
# Copy the requirements file
COPY prerequisites.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/packages -r prerequisites.txt && \
    pip install --no-cache-dir --prefix=/packages --upgrade six

FROM python:3.13.6-slim

WORKDIR /app

# Copy packages and app
COPY --from=builder /packages /usr/local
COPY app/ .

# Expose the port used by the OPC UA server simulator
EXPOSE 4840

# Run the command to start the OPC UA server simulator when the container launches
CMD ["python", "opc_ua_server_simulator.py"]
