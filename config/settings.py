from dotenv import load_dotenv
import os

load_dotenv()

NETBOX_URL = os.getenv("NETBOX_URL")
NETBOX_TOKEN = os.getenv("NETBOX_TOKEN")

DEVICE_USERNAME = os.getenv("DEVICE_USERNAME")
DEVICE_PASSWORD = os.getenv("DEVICE_PASSWORD")

# Basic validation (important in enterprise code)
if not NETBOX_URL or not NETBOX_TOKEN:
    raise ValueError("NetBox credentials are missing!")

if not DEVICE_USERNAME or not DEVICE_PASSWORD:
    raise ValueError("Device credentials are missing!")