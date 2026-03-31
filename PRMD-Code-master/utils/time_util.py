"""
Created by Martin McLaren c2645410
No AI was used in the creation of this code
"""
from datetime import datetime

def unix_to_iso(unix_time: float) -> str:
    """

    Args:
        unix_time: The unix time to convert into ISO format.

    Returns: The unix time given in an iso format

    """
    date_time = datetime.fromtimestamp(unix_time)
    return date_time.isoformat()
