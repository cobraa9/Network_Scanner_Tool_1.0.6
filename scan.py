from scapy.all import ARP, Ether, srp, wrpcap

def scan_network(target_ip):
    #"""Performs an ARP scan on the target IP or subnet."""
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=5, verbose=0)[0]

    clients = [{"ip": received.psrc, "mac": received.hwsrc} for sent, received in result]
    
    return clients

def save_to_pcap(clients, filename):
    #"""Saves the scanned network data as a PCAP file."""
    packets = []
    for client in clients:
        arp = ARP(pdst=client["ip"], hwdst=client["mac"])
        ether = Ether(dst=client["mac"])
        packet = ether / arp
        packets.append(packet)

    if packets:
        wrpcap(filename, packets)
        print(f"Captured packets saved to {filename}")
    else:
        print("No valid packets to save")

def print_scan_results(clients):
    #"""Prints the list of discovered network devices."""
    print("Available devices on the network:")
    print("IP" + " "*18 + "MAC")
    for client in clients:
        print("{:16}     {}".format(client["ip"], client["mac"]))

if __name__ == "__main__":
    target_ip = input("Enter the IP address or subnet to scan (e.g., 192.168.1.0/24): ")

    clients = scan_network(target_ip)
    print_scan_results(clients)

    filename = input("Enter the filename to save the captured packets (e.g., network_scan.pcap): ")
    save_to_pcap(clients, filename)
