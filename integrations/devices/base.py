from netmiko import ConnectHandler
import logging
from typing import Optional

from config.settings import DEVICE_USERNAME, DEVICE_PASSWORD


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class NetworkConnection:

    def __init__(self, device_ip: str, device_type: str):
        self.device_ip = device_ip
        self.device_type = device_type
        self.connection: Optional[ConnectHandler] = None

    def connect(self) -> bool:
        try:
            self.connection = ConnectHandler(
                device_type=self.device_type,
                host=self.device_ip,
                username=DEVICE_USERNAME,
                password=DEVICE_PASSWORD,
            )
            logger.info(f"Connected to {self.device_ip}")
            return True
        except Exception as e:
            logger.error(f"Connection failed to {self.device_ip}: {e}")
            return False

    def send_command(self, command: str) -> str:
        """
        Execute show commands
        """
        if not self.connection:
            raise ConnectionError("Not connected to device")

        try:
            output = self.connection.send_command(command)
            return output
        except Exception as e:
            logger.error(f"Command failed: {command} | Error: {e}")
            return ""

    def send_config(self, config_commands: list) -> str:
        """
        Push configuration
        """
        if not self.connection:
            raise ConnectionError("Not connected to device")

        try:
            output = self.connection.send_config_set(config_commands)
            logger.info(f"Config pushed to {self.device_ip}")
            return output
        except Exception as e:
            logger.error(f"Config push failed: {e}")
            return ""

    def disconnect(self):
        """
        Close connection
        """
        if self.connection:
            self.connection.disconnect()
            logger.info(f"Disconnected from {self.device_ip}")
