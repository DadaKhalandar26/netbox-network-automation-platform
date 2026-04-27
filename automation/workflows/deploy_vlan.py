from netbox.client import NetBoxClient
from automation.base.connection import NetworkConnection
from automation.services.vlan import generate_vlan_config


def deploy_vlan(device_name: str, vlan_id: int):
    nb = NetBoxClient()

    # 🔷 Get device IP
    device_ip = nb.get_device_ip(device_name)
    if not device_ip:
        print(f"Device {device_name} IP not found")
        return

    # 🔷 Get VLAN from NetBox
    vlan = nb.get_vlan(vlan_id)
    if not vlan:
        print(f"VLAN {vlan_id} not found in NetBox")
        return

    vlan_name = vlan.get("name")

    print(f"Deploying VLAN {vlan_id} ({vlan_name}) to {device_name}")

    # 🔷 Generate config
    config = generate_vlan_config(vlan_id, vlan_name)

    print("Generated Config:")
    for line in config:
        print(line)

    # 🔷 Connect to device
    conn = NetworkConnection(device_ip, "cisco_ios")

    if conn.connect():
        output = conn.send_config(config)
        print("Device Output:")
        print(output)

        conn.disconnect()
    else:
        print("Connection failed")
