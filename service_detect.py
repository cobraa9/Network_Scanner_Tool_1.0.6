import socket

def get_service_banner(target_ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target_ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return None
