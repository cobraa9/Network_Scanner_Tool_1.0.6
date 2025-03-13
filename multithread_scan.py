import socket
import threading

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        s.close()
        if result == 0:
            print(f"Port {port} is open")
    except:
        pass

def multithread_scan(target_ip, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
