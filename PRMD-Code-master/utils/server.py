"""
Created in part by Martin McLaren c2645410
No AI was used in the creation of this code
"""
import settings
from communication.client import get_iot_hub_client
from communication.upload import run_upload

def upload_data():
    connection_string = settings.IOT_CONNECTION_STRING
    client = get_iot_hub_client(connection_string)
    run_upload(client)