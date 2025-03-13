from scan import scan_network
from service_scan import detect_services  # Updated function import
from multithread_scan import multithread_scan
from stealth_scan import stealth_scan
from save_results import save_to_json, save_to_csv, save_to_pcap

def main():
    target_ip = input("Enter the IP address or subnet to scan (e.g., 192.168.1.0/24): ")

    print("\nSelect scanning method:")
    print("1. Network Scan (Find active devices)")
    print("2. Service Detection (Find running services)")
    print("3. Multithreaded Port Scan (Faster scanning)")
    print("4. Stealth Scan (Avoid detection)")
    
    choice = input("Enter your choice (1-4): ")
    results = []

    if choice == "1":
        results = scan_network(target_ip)
        print("\nNetwork Scan Results:")
        for client in results:
            print(f"IP: {client['ip']} - MAC: {client['mac']}")

    elif choice == "2":
        print("\nPerforming Service Detection...")
        results = detect_services(target_ip)  # Call `detect_services`

        if results:
            print("\nService Detection Results:")
            print("PORT\tSERVICE\t\tBANNER")
            for port, info in results.items():
                print(f"{port}\t{info['service']}\t{info['banner']}")
        else:
            print("\nNo open services detected.")

    elif choice == "3":
        print("\nPerforming Multithreaded Port Scan...")
        results = multithread_scan(target_ip, range(20, 1025))

    elif choice == "4":
        print("\nPerforming Stealth Scan...")
        for port in range(20, 1025):
            scan_result = stealth_scan(target_ip, port)
            print(scan_result)
            results.append({"ip": target_ip, "port": port, "status": scan_result})

    else:
        print("Invalid choice! Exiting...")
        return

    # Ask if the user wants to save results
    if results:
        print("\nSelect format to save results:")
        print("1. JSON")
        print("2. CSV")
        print("3. PCAP")

        save_choice = input("Enter your choice (1-3): ")
        filename = input("Enter filename (without extension): ")

        if save_choice == "1":
            save_to_json(results, filename + ".json")
        elif save_choice == "2":
            save_to_csv(results, filename + ".csv")
        elif save_choice == "3":
            save_to_pcap(results, filename + ".pcap")
        else:
            print("Invalid choice! Results not saved.")

if __name__ == "__main__":
    main()
