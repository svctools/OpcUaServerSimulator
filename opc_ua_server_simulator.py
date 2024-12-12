# OPC-UA Server with simulated sensor values
# https://github.com/FreeOpcUa/python-opcua

import asyncio
import logging
import os
from datetime import datetime

import pandas as pd
from asyncua import Server
from asyncua.ua import NodeId

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("asyncua")


async def main():
    try:
        idx, server = await setup_server()
        sensor_data = await get_data_frame()

        line = await server.nodes.objects.add_object(NodeId("Production/Line1", idx), "Line1")
        fan = await line.add_object(NodeId("Production/Line1/fan1", idx), "fan1")
        product = await line.add_object(NodeId("Production/Line1/product", idx), "product")

        air_flow_actual = await fan.add_variable(
            NodeId("Production/Line1/fan1/air_flow_actual", idx), "air_flow_actual", val=0
        )
        speed_percent_set = await fan.add_variable(
            NodeId("Production/Line1/fan1/speed_percent_set", idx), "speed_percent_set", 0
        )
        line_mode_code = await line.add_variable(
            NodeId("Production/Line1/line_mode/line_mode_code", idx), "line_mode_code", 0
        )
        product_code = await product.add_variable(
            NodeId("Production/Line1/product/product_code", idx), "product_code", 0
        )
        product_name = await product.add_variable(
            NodeId("Production/Line1/product/product_name", idx), "product_name", ""
        )
        utc_timestamp = await line.add_variable(
            NodeId("Production/Line1/utc_timestamp", idx), "utc_timestamp", ""
        )

        _logger.info("Starting OPC UA Server Simulator")
        async with server:
            while True:
                for row in sensor_data.itertuples():
                    await air_flow_actual.write_value(float(row[1]))
                    await speed_percent_set.write_value(float(row[2]))
                    await line_mode_code.write_value(int(row[3]))
                    await product_code.write_value(str(row[4]) if row[4] else "")
                    await product_name.write_value(str(row[5]))
                    await utc_timestamp.write_value(datetime.utcnow().isoformat())
                    await asyncio.sleep(1)

    except Exception as e:
        _logger.error(f"An error occurred: {e}")
        raise


async def get_data_frame():
    """
    Reads and validates the measurements CSV file.
    :return: Pandas DataFrame
    """
    csv_path = os.getenv("MEASUREMENTS_CSV", "measurements.csv")
    try:
        df = pd.read_csv(csv_path)
        required_columns = [
            "sensor_03",
            "sensor_01",
            "line_mode_code",
            "product_code",
            "product_name",
        ]
        if not all(column in df.columns for column in required_columns):
            raise ValueError(f"CSV file must contain the following columns: {required_columns}")
        return df[required_columns]
    except Exception as e:
        _logger.error(f"Failed to load or validate the CSV file: {e}")
        raise


async def setup_server():
    """
    Sets up the OPC-UA server and its namespace.
    :return: namespace index and server instance
    """
    server = Server()
    await server.init()
    server.set_endpoint(os.getenv("OPCUA_ENDPOINT", "opc.tcp://0.0.0.0:4840/opcua/"))
    server.set_server_name("Simulated OPC-UA Server")
    uri = os.getenv("OPCUA_NAMESPACE_URI", "http://simulatedopcserver.com/opcua/")
    idx = await server.register_namespace(uri)
    return idx, server


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        _logger.info("Server shutdown initiated by user.")
