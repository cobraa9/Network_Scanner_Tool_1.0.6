import socket
from scapy.all import sr1, IP, TCP

COMMON_PORTS = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP",
                110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP"}

def detect_services(target_ip):
    #"""Detects running services by scanning common ports and grabbing banners."""
    print("\nScanning for open services...\n")
    open_services = {}

    for port, service_name in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout for faster scanning
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            try:
                sock.send(b'Hello\r\n')  # Send a basic request
                banner = sock.recv(1024).decode().strip()  # Grab banner
            except:
                banner = "No Banner"
            
            open_services[port] = {"service": service_name, "banner": banner}
        
        sock.close()

    return open_services

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan for services: ")
    results = detect_services(target_ip)

    if results:
        print("\nService Detection Results:")
        print("PORT\tSERVICE\t\tBANNER")
        for port, info in results.items():
            print(f"{port}\t{info['service']}\t{info['banner']}")
    else:
        print("\nNo open services detected.")
