from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "../../templates/cisco")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def generate_vlan_config(vlan_id: int, vlan_name: str) -> list:
    """
    Generate VLAN config using Jinja2
    """
    template = env.get_template("vlan.j2")

    config = template.render(
        vlan_id=vlan_id,
        vlan_name=vlan_name
    )

    # Convert to list for Netmiko
    return config.splitlines()
