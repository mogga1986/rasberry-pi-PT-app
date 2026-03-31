from datetime import datetime
from typing import Dict


class Message:
    """
    Represents a formatted message for transmission.

    Converts raw sensor data into a structured dictionary suitable for communication.
    """

    def __init__(
        self,
        raw_data: Dict[str, int],
        session_id: str,
        timestamp: str,
        sensor_type: str = "unknown",
    ):
        self.raw_data = raw_data
        self.session_id = session_id
        self.sensor_type = sensor_type
        self.timestamp = self._format_timestamp(timestamp)

    def _format_timestamp(self, ts: str) -> str:
        """
        Converts a Unix timestamp string to ISO 8601 format with UTC.

        Args:
            ts (str): The timestamp string from the raw data.

        Returns:
            str: ISO 8601 formatted string with 'Z' for UTC.
        """
        dt = datetime.fromtimestamp(float(ts))
        return dt.isoformat()

    def to_dict(self) -> Dict[str, int | str]:
        """
        Converts the message into the required dictionary format.

        Returns:
            dict: The formatted message dictionary.
        """
        formatted = {}

        for key, value in self.raw_data.items():
            parts = key.split("_")
            if len(parts) == 3:  # Normalise labels
                location, sensor_type, axis = parts
                label = f"{location.lower()}_{sensor_type.lower()}_{axis.lower()}"  # Just in case we change format
            else:
                # fallback for unexpected keys
                label = key

            formatted[label] = value

        formatted["SessionID"] = self.session_id
        formatted["Timestamp"] = self.timestamp
        formatted["SensorType"] = self.sensor_type

        return formatted

    def print_message(self):
        """
        Prints the keys and types of values in the formatted message dictionary.

        This helps visualize the structure (shape) of the message for debugging or documentation.
        """
        formatted = self.to_dict()
        print("Message shape:")
        for key, value in formatted.items():
            print(f"  {key}: {value}")
