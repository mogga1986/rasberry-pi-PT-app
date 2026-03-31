from azure.iot.device import IoTHubDeviceClient


def get_iot_hub_client(connection_string: str) -> IoTHubDeviceClient:
    """
    Create an IoTHubDeviceClient instance.

    This function creates an instance of the IoTHubDeviceClient using the provided connection string.
    It is used to establish a connection to Azure IoT Hub for sending messages.

    Args:
        connection_string (str): The connection string for the Azure IoT Hub.

    Returns:
        IoTHubDeviceClient: An instance of the IoTHubDeviceClient.
    """
    return IoTHubDeviceClient.create_from_connection_string(connection_string)
