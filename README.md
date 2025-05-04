# Network Scanner Tool (1.0.6)💻
![network_scanner_resized](https://github.com/user-attachments/assets/038cb24c-6fae-4dad-bfb0-9f6d478b7808)

## Overview 

The **Network Scanner Tool** is a Python-based cybersecurity tool designed to scan networks, detect open ports, banner grabbing, identify running services, and assess potential vulnerabilities. As a beginner, this tool is ideal for  network security students and cybersecurity researchers  who want to analyze their networks. 


# Features Update in Version 1.0.6   

✅ **Fastrer Scan:**  
- Uses Python's `threading` library to scan multiple targets simultaneously, reducing scan time significantly.  

✅ **Stealth Scan:**  
- Uses a SYN scan (half-open scan) to avoid detection by IDS/IPS.  
- The connection is not fully established, making it harder to detect.  

✅ **Improved Port Scanning:**  
- Enhanced accuracy in detecting open ports and identifying the services running on them.  
- Added support for UDP and TCP port scanning.  

✅ **Enhanced Reporting:**  
- Option to export scan results in **PCAP**, **JSON**, or **CSV** format for better analysis and sharing.  
- Improved formatting and detail level in reports.  

---

## Technologies and Libraries Used   

- **Python:** Core programming languagefor the script. LINK --> https://www.python.org/downloads/  
- **Scapy:** Used for packet creation, sniffing, and analysis. LINK --> https://github.com/secdev/scapy  
- **socket:** Built-in Python module for network communications.  
- **nmap (python-nmap):** Enhances port scanning and service detection. LINK --> https://nmap.org/download.html  
- **argparse:** For handling command-line arguments.  
- **subprocess:** To execute system commands for additional functionalities.  
- **threading:** Used to enable multithreading for faster scanning.   
- **pcapviewer:** To analyze the network PCAP/PCAPNG (Packet Capture) files. LINK --> https://marketplace.visualstudio.com/items?itemName=sankooc.pcapviewer  

---

## Installation 📥  

### Prerequisites   
Make sure that you have installed Python 3.x.y (any updated version)  on your system.   

```bash
py --version
```

### Clone the Repository   

```bash
git clone https://github.com/cobraa9/Network_Scanner_Tool_1.0.5.git
cd Network_Scanner_Tool_1.0.5
```

### Install Required Libraries   

```bash
pip install scapy python-nmap argparse
```

---

## Usage   

Run the tool with the following command and enter your target IP for scanning:  

```bash
python main.py
 192.168.1.100/24
```

---

### Command-Line Arguments(Optional)   

| Argument         | Description                                              |
|------------------|----------------------------------------------------------|
| `--target`        | The target IP address or subnet to scan.                 |
| `--ports`         | Specific ports to scan (default: common ports).           |
| `--stealth`       | Perform a stealthy SYN scan (to avoid detection).         |
| `--threads`       | Number of threads to use for faster scanning.             |
| `--output`        | Save the scan results to a file (PCAP/JSON/CSV format).   |

---

### Example Commands   

- Scan a specific IP:  
```bash
python main.py
--target 192.168.1.100
```

- Perform a stealth scan on a target IP (or by choosing option 4):  
```bash
python main.py
192.168.1.100 --stealth
```

- Scan using multithreading (or by choosing option 3):  
```bash
python main.py
 192.168.1.0/24 --threads 10
```

- After the scan if there are any captured packets, save results to PCAP/JSON/CSV(.pcap format recommended for better result analysis)by choosing any prefered option 1, 2 or 3 :  
```bash
python main.py
 192.168.1.0/24
 1
--output results.pcap
```

---

## How It Works   

1. **Device Discovery:**  
   Uses ARP requests to detect active devices on the network.   

2. **Port Scanning:**  
   - Uses TCP SYN scans to identify open ports.   
   - Optionally performs UDP scans for additional coverage.  

3. **Service Detection:**  
   Uses Nmap integration to identify running services.   

4. **Stealth Scan:**  
   Performs a half-open SYN scan to avoid detection by firewalls.   

5. **Faster Scan:**  
   Scans multiple targets simultaneously, improving scan efficiency.   

6. **Vulnerability Detection:**  
   Cross-references detected services with a known vulnerability database.  

7. **Report Generation:**  
   Saving Outputs findings in a structured format (PCAP, JSON, or CSV).  

---

## Disclaimer ⚠️  

This tool is intended for **educational and ethical** purposes only. While port scanning itself isn't always illegal, but unauthorized scanning of networks that you do not own or have permission to scan is illegal and punishable by law.   

---

## Contribution 🤝  

This is an updated version from my previous project , and Contributions are welcome! Feel free to fork the repository and submit pull requests. 📝  

###  **Future Plans:**  
👉 **GUI Integration:** Planning to create a user-friendly GUI using **Tkinter** or **PyQt** to improve usability and user experience.  
👉 **Plugin System:** Planning to add support for custom scanning modules.  
👉 **Advanced Report Generate:** Planning to update more features for better packet capturing and result analysis.
---

## Author   

**Anirban**  

For Suggestions, feel free to contact me via GitHub. 📩  

---
