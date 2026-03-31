import settings


class Session:
    """
    Represents a session of data collection from a specific sensor.

    This class is responsible for managing the session ID and the data points collected during the session.
    It provides methods to create a session from JSON data, generate a unique session ID, and retrieve session information.
    The session ID is generated based on the device ID and the earliest timestamp in the data points.
    The session data is stored as a list of dictionaries, each containing a timestamp and the corresponding data.

    Attributes:
        session_id (str): The unique identifier for the session.
        data_points (list[dict]): A list of dictionaries containing the timestamp and data collected during the session.
    """

    def __init__(self, session_id: str, data_points: list[dict]):
        self.data_points = data_points
        self.session_id = self.generate_session_id(settings.DEVICE_ID)

    @classmethod
    def from_json(cls, json_data: dict) -> "Session":
        """
        Create a Session instance from JSON data.

        This method takes a JSON object containing session information and converts it into a Session instance.
        The JSON data should contain a session ID and a list of data points, each with a timestamp and sensor type.

        Args:
            json_data (dict): The JSON data containing session information.

        Returns:
            Session: An instance of the Session class initialized with the provided JSON data.
        """
        data_points = []
        for sensor_type, readings in json_data.items():
            for timestamp, data in readings.items():
                data_points.append(
                    {
                        "timestamp": timestamp,
                        "sensor_type": sensor_type,
                        "data": data if isinstance(data, dict) else {"data": data},
                    }
                )

        return cls(
            session_id=json_data.get("session_id", "unknown"), data_points=data_points
        )

    def generate_session_id(self, device_id: str) -> str:
        """
        Generate a unique session ID based on the device ID and the earliest timestamp in the data points.

        The session ID is a combination of the device ID and the earliest timestamp in the data points.
        The timestamp is converted to a string and appended to the device ID.

        Args:
            device_id (str): The unique identifier for the device.

        Returns:
            str: The generated session ID.

        Raises:
            ValueError: If there are no data points available to generate the session ID.
        """

        if not self.data_points:
            raise ValueError("No data points available to generate session ID.")

        earliest_ts = min(dp["timestamp"] for dp in self.data_points)
        ts_str = str(int(float(earliest_ts)))

        session_id = f"{device_id}_{ts_str}"
        return session_id

    def get_session_id(self) -> str:
        """
        Get the session ID.

        Returns:
            str: The session ID.
        """
        return self.session_id

    def get_all_datapoints(self) -> list:
        """
        Get all data points in the session.

        Returns:
            list: A list of all data points in the session.
        """
        return self.data_points

    def to_string(self) -> str:
        """
        Convert the session data to a string representation.

        Returns:
            str: A string representation of the session data.
        """
        return f"Session ID: {self.session_id}, Data Points: {self.data_points}"
