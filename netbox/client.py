import pynetbox
import logging
from typing import List, Dict, Optional

from config.settings import NETBOX_URL, NETBOX_TOKEN


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class NetBoxClient:
    """
    NetBox API Client (Enterprise-ready)
    """

    def __init__(self):
        if not NETBOX_URL or not NETBOX_TOKEN:
            raise ValueError("NetBox credentials missing")

        try:
            self.nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)
            logger.info("Connected to NetBox")
        except Exception as e:
            logger.error(f"Failed to connect to NetBox: {e}")
            raise

    # 🔷 Get all devices
    def get_devices(self) -> List[Dict]:
        try:
            devices = self.nb.dcim.devices.all()
            return [device.serialize() for device in devices]
        except Exception as e:
            logger.error(f"Error fetching devices: {e}")
            return []

    # 🔷 Get device by name
    def get_device(self, name: str) -> Optional[Dict]:
        try:
            device = self.nb.dcim.devices.get(name=name)
            return device.serialize() if device else None
        except Exception as e:
            logger.error(f"Error fetching device {name}: {e}")
            return None

    # 🔷 Get device primary IP
    def get_device_ip(self, device_name: str) -> Optional[str]:
        try:
            device = self.nb.dcim.devices.get(name=device_name)

            if device and device.primary_ip:
                return str(device.primary_ip.address).split("/")[0]

            logger.warning(f"No IP found for device {device_name}")
            return None

        except Exception as e:
            logger.error(f"Error fetching IP for {device_name}: {e}")
            return None

    # 🔷 Get VLANs
    def get_vlans(self) -> List[Dict]:
        try:
            vlans = self.nb.ipam.vlans.all()
            return [vlan.serialize() for vlan in vlans]
        except Exception as e:
            logger.error(f"Error fetching VLANs: {e}")
            return []

    # 🔷 Get VLAN by ID
    def get_vlan(self, vid: int) -> Optional[Dict]:
        try:
            vlan = self.nb.ipam.vlans.get(vid=vid)
            return vlan.serialize() if vlan else None
        except Exception as e:
            logger.error(f"Error fetching VLAN {vid}: {e}")
            return None
