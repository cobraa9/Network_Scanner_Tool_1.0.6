import json
import csv
from scapy.all import ARP, Ether, wrpcap

def save_to_json(results, filename):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {filename}")

def save_to_csv(results, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ip", "port", "service"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {filename}")

def save_to_pcap(results, filename):
    packets = []
    for result in results:
        if "ip" in result and "port" in result:
            arp = ARP(pdst=result["ip"])
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            packets.append(packet)

    if packets:
        wrpcap(filename, packets)
        print(f"Captured packets saved to {filename}")
