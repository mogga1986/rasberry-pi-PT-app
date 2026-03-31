"""
Created in part by Martin McLaren c2645410
No AI was used in the creation of this code
"""
import os
from dotenv import load_dotenv

load_dotenv()

# .env files
IOT_CONNECTION_STRING = os.getenv("IOT_CONNECTION_STRING")
DEVICE_ID = os.getenv("DEVICE_ID")

# Configuration settings
POLLING_RATE = 1  # time in seconds between reads
DEBUG = True

# Directories
DATA_DIR = "data"
SESSION_DIR = "data/sessions"
