import netifaces as ni

# Replace 'eth0' with your network interface name (e.g., 'wlan0' for Wi-Fi).
interface_name = 'eth0'

try:
    # Get the MAC address for the specified interface
    mac_address = ni.ifaddresses(interface_name)[ni.AF_LINK][0]['addr']
    print(f"MAC Address of {interface_name}: {mac_address}")
except ValueError:
    print(f"Could not retrieve MAC Address for {interface_name}")
