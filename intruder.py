# Network Intruder Alert System
# Real-time WiFi device monitor
# Author: rudranoir0-dot

from scapy.all import ARP, Ether, srp
import time
from datetime import datetime

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })
    return devices

def get_ip_range():
    return "172.20.10.1/28"

print("=" * 50)
print("   NETWORK INTRUDER ALERT SYSTEM")
print("=" * 50)

ip_range = get_ip_range()
print(f"\nMonitoring network: {ip_range}")
print("Learning trusted devices...\n")

trusted_devices = {}
initial_scan = scan_network(ip_range)
for device in initial_scan:
    trusted_devices[device["mac"]] = device["ip"]
    print(f"  [TRUSTED] {device['ip']} -- {device['mac']}")

print(f"\n{len(trusted_devices)} trusted devices registered.")
print("\nWatching for intruders... Press Ctrl+C to stop\n")

while True:
    time.sleep(30)
    current_devices = scan_network(ip_range)
    for device in current_devices:
        mac = device["mac"]
        ip = device["ip"]
        if mac not in trusted_devices:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[!!!] INTRUDER DETECTED at {timestamp}")
            print(f"      IP  : {ip}")
            print(f"      MAC : {mac}")
            print(f"      ACTION: Block this device on your router!\n")
            trusted_devices[mac] = ip