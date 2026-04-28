from integrations.netbox.client import get_devices, get_vlan
from integrations.devices.base import connect
from services.vlan_service import ensure_vlan


def deploy_vlan(vlan_id: int):
    devices = get_devices()
    vlan = get_vlan(vlan_id)

    if not vlan:
        raise ValueError(f"VLAN {vlan_id} not found in NetBox")

    for device in devices:
        try:
            # Extract IP safely
            if not device.primary_ip:
                print(f"[SKIP] {device.name} has no IP")
                continue

            ip = str(device.primary_ip.address).split("/")[0]

            print(f"[INFO] Connecting to {device.name} ({ip})")

            conn = connect(ip)

            result = ensure_vlan(conn, vlan_id, vlan.name)

            print(f"[SUCCESS] {device.name}: VLAN {vlan_id} -> {result}")

            conn.disconnect()

        except Exception as e:
            print(f"[ERROR] {device.name}: {str(e)}")