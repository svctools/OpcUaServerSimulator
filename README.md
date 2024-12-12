# Documentation for Simulated OPC-UA Server 🌟🌐✨

This document provides detailed information about the Python-based OPC-UA server implemented using the `asyncua` library. The server simulates sensor data and exposes it via an OPC-UA interface for testing and integration purposes. 📚📊💡

## Overview 🌍🔍🛠️

The OPC-UA server simulates sensor data for a production line. It periodically updates values for variables such as air flow, speed percentage, line mode, and product information. Data is sourced from a CSV file, which represents time-series measurements. 📈📋📂

### Key Features ✅📌✨
- Simulates real-time sensor data for an OPC-UA server.
- Reads sensor data from a configurable CSV file.
- Dynamically updates OPC-UA nodes with simulated values.
- Gracefully handles server shutdown.
- Highly configurable using environment variables.

## Code Structure 🖥️📂🔧

### Modules and Libraries 📦📚⚙️
- **asyncua**: Used to implement the OPC-UA server and define nodes.
- **pandas**: Processes the CSV file containing the sensor data.
- **asyncio**: Handles asynchronous operations for server functionality.
- **logging**: Provides logging capabilities for server operations.
- **os**: Manages environment variables for configuration.
- **signal**: Handles system signals for graceful shutdown.
- **datetime**: Provides timestamps for sensor data.

### Main Components 🚀🔑⚙️

#### `main()` 🏁📜🛠️
This is the main entry point of the application. It:
- Sets up the OPC-UA server and its namespace.
- Creates OPC-UA objects and variables to simulate sensor data.
- Iterates over the data from the CSV file, updating OPC-UA nodes with new values.
- Runs the server indefinitely while simulating real-time behavior.

#### `setup_server()` 🏗️🔧🌐
Initializes and configures the OPC-UA server, including:
- Setting the server endpoint and name.
- Registering a namespace.

#### `get_data_frame()` 📖📊⚡
Reads the CSV file containing simulated sensor data and validates it. Extracts only the required columns for the simulation.

#### `graceful_shutdown(loop)` 🛑🔔✅
Handles graceful shutdown of the server by:
- Cancelling all running tasks.
- Stopping the event loop.

## Environment Variables 🌐⚙️📋
The server supports configuration using environment variables: 📂🛠️🖥️

| Variable                | Default Value                          | Description                              |
|-------------------------|----------------------------------------|------------------------------------------|
| `MEASUREMENTS_CSV`      | `measurements.csv`                    | Path to the CSV file containing sensor data. |
| `OPCUA_ENDPOINT`        | `opc.tcp://0.0.0.0:4840/opcua/`       | Server endpoint URL.                     |
| `OPCUA_NAMESPACE_URI`   | `http://simulatedopcserver.com/opcua/` | Namespace URI for the OPC-UA server.     |

## CSV File Requirements 📄📋📂
The CSV file must contain the following columns: 🗂️✅✨

| Column Name       | Description                                           |
|-------------------|-------------------------------------------------------|
| `sensor_03`       | Simulated air flow actual values.                     |
| `sensor_01`       | Simulated speed percentage set values.                |
| `line_mode_code`  | Simulated mode code of the production line.           |
| `product_code`    | Product code associated with the production process.  |
| `product_name`    | Product name associated with the production process.  |

Example CSV content: 📝🖋️📊
```csv
sensor_03,sensor_01,line_mode_code,product_code,product_name
5.3,70,1,P001,Product_1
6.1,80,1,P001,Product_1
0.0,0,2,,
```

## How to Run ▶️⚙️💻

1. Install the required dependencies: 📥📦⚡
   ```bash
   pip install -r prerequisities.txt
   ```

2. Prepare the CSV file with the required columns or use original one. 📂📝✅

3. (Optional) Set environment variables: 🔧🌐🖥️
   ```bash
   export MEASUREMENTS_CSV=/path/to/your/file.csv
   export OPCUA_ENDPOINT=opc.tcp://localhost:4840/opcua/
   export OPCUA_NAMESPACE_URI=http://customnamespace.com/opcua/
   ```

4. Run the server: 🏃‍♂️🚀✨
   ```bash
   python opc_ua_server_simulator.py
   ```

## How to Run via docker container▶️⚙️💻

1. Build docker container base on Dockerfile: 📥📦⚡

2. Run the docker container via command 📂📝✅
  ```bash
   docker run -d -p 4840:4840 opcuaserversimulator
   ```
## Server Behavior ⚙️🔄🌟
- The server starts and initializes the OPC-UA namespace. 🚦🔧🌐
- Reads the CSV file to simulate sensor data. 📖📂📊
- Periodically updates OPC-UA variables with new values. 🔄🖋️📋
- Provides a real-time interface for clients to connect and read simulated data. 🕒🖥️🤝

## Logging 📝📈🔍
Logs are displayed in the console at the INFO level. Key events, errors, and warnings are logged for debugging and monitoring purposes. 🔑❌⚠️

## Graceful Shutdown 🛑🔔✅
The server handles `SIGINT` (Ctrl+C) and `SIGTERM` signals to:
- Cancel all running tasks. ❌🔄✅
- Stop the event loop. 🛑⚙️💡
- Ensure a clean exit. 🌟✅🖥️

## Extending the Server ➕🔄✨

### Adding New Variables 🖋️📋🔑
1. Define a new variable in the desired object using the `add_variable` method. 🛠️🖥️✅
2. Update the simulation loop to write values to the new variable. 🔄✍️📊

### Changing Data Sources 🔄🗂️🔧
To use a different data source, modify the `get_data_frame()` function to fetch data from a new source (e.g., a database or API). 📂🌐⚡

## Troubleshooting 🔍❌💡

### Common Issues ⚠️🔑✨
| Problem                               | Possible Cause                         | Solution                                |
|---------------------------------------|----------------------------------------|----------------------------------------|
| Server not starting                   | Port conflict or invalid endpoint.     | Check and update the `OPCUA_ENDPOINT`. |
| CSV file not found or invalid columns | File path or content issue.            | Verify file path and structure.        |
| Server stops unexpectedly             | Unhandled exception or resource issue. | Check logs for error details.          |

## Conclusion 🌟🏁📚
This OPC-UA server provides a simple yet powerful way to simulate production line data. It can be extended to suit various testing and development scenarios. For further customization, modify the simulation logic, data source, or OPC-UA variables as needed. 🛠️📈✨