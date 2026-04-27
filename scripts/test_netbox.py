from netbox.client import NetBoxClient

nb = NetBoxClient()

# Test connection
devices = nb.get_devices()
print(f"Total devices: {len(devices)}")

# Test specific device
device = nb.get_device("hyd-access-1")
print(device)

# Test IP
ip = nb.get_device_ip("hyd-wan-1")
print("Device IP:", ip)

# Test VLAN
vlan = nb.get_vlan(10)
print(vlan)
