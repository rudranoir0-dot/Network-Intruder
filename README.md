# Network Intruder Alert System

A real-time network monitoring tool that detects unknown devices 
connecting to your WiFi and alerts you instantly.

## How it works

- Scans your network every 30 seconds using ARP protocol
- Learns all trusted devices on first run
- The moment an unknown device connects — fires an instant alert
- Shows IP address, MAC address and timestamp of the intruder

## Usage

Install dependency:

pip install scapy

Run the monitor:

python intruder.py

## Example Output

==================================================

NETWORK INTRUDER ALERT SYSTEM
Monitoring network: 172.20.10.1/28

Learning trusted devices...
[TRUSTED] 172.20.10.3 -- 9c:da:3e:03:00:e3

[TRUSTED] 172.20.10.1 -- aa:9c:78:a6:c4:64
2 trusted devices registered.

Watching for intruders... Press Ctrl+C to stop
[!!!] INTRUDER DETECTED at 2026-06-19 11:44:00

IP  : 172.20.10.2

MAC : 46:bc:79:8e:af:a8

ACTION: Block this device on your router!

## Concepts used

- ARP (Address Resolution Protocol)
- MAC address identification
- Real-time network monitoring
- Intrusion detection logic

## Author

rudranoir0-dot | CSE Cyber Security | 