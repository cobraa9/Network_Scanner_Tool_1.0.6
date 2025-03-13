from scapy.all import sr1, IP, TCP

def stealth_scan(target_ip, port):
    stealth_pkt = IP(dst=target_ip)/TCP(dport=port, flags="S")  # SYN packet
    response = sr1(stealth_pkt, timeout=1, verbose=0)

    if response and response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # SYN-ACK received
            return f"Port {port} is open"
        elif response.getlayer(TCP).flags == 0x14:  # RST received
            return f"Port {port} is closed"
    return f"Port {port} is filtered or no response"
