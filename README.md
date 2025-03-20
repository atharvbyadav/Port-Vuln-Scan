# **Port-Vuln-Scan**  
*A powerful, lightweight network reconnaissance tool for open port scanning and vulnerability detection.*  

## **📌 Overview**  
**Port-Vuln-Scan** is a **Python-based security tool** designed for **network penetration testing** and **security assessments**. It enables ethical hackers, system administrators, and cybersecurity professionals to:  

✔️ **Identify open ports** on a target system  
✔️ **Detect running services** on those ports  
✔️ **Check for potential vulnerabilities** in identified services  

The tool is modular, meaning **each script serves a specific function** in the reconnaissance process.  

## **⚡ Features**  
✅ **Fast Port Scanning** (with single-threaded & multi-threaded options)  
✅ **Service Detection** (identifies services running on open ports)  
✅ **Multi-threading Support** (for optimized scanning performance)  
✅ **Vulnerability Lookup** (checks services against known vulnerabilities)  
✅ **Standalone Execution** (each script runs independently)  

---

## **📥 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/atharvbyadav/Port-Vuln-Scan.git
cd Port-Vuln-Scan
```

### **2️⃣ Install Required Dependencies**  
Ensure you have **Python 3** installed, then install required modules:  
```bash
pip install requests
```

### **3️⃣ Make Scripts Executable**  
Each script includes `#!/usr/bin/python3`, allowing direct execution:  
```bash
chmod +x banner.py ports.py ports2.py vulnscan.py
```

---

## **🚀 Usage Guide**  
Each script serves a **unique role** in the scanning process.  

---

### **1️⃣ banner.py - Display the ASCII Art Banner**  
📌 **Purpose:** Displays an ASCII banner when running the tool, making it visually appealing.  
🔧 **How It Works:**  
- The script prints an ASCII-style welcome message.  
- It helps in branding and making the tool more user-friendly.  

#### **Run Command:**  
```bash
./banner.py
```

---

### **2️⃣ ports.py - Basic Port Scanner**  
📌 **Purpose:** Scans **common ports** to check if they are open on a target machine.  
🔧 **How It Works:**  
- Uses the `socket` library to attempt a **TCP connection** to a list of ports.  
- If a connection is successful, the port is reported as **open**.  
- Runs **sequentially**, meaning it **scans one port at a time**.  

#### **Run Command:**  
```bash
./ports.py <target-ip>
```
Example:  
```bash
./ports.py -h 192.168.1.1
```

🛠 **Use Case:** This script is useful for quickly checking which **standard ports** are open before conducting a detailed scan.  

---

### **3️⃣ ports2.py - Multi-threaded Port Scanner**  
📌 **Purpose:** A **faster version** of `ports.py` that leverages **multi-threading** for parallel port scanning.  
🔧 **How It Works:**  
- Uses **multiple threads** to **scan multiple ports simultaneously**.  
- Reduces scan time significantly, making it ideal for large networks.  
- Automatically handles **timeouts** to prevent hanging on unresponsive ports.  

#### **Run Command:**  
```bash
./ports2.py <target-ip>
```
Example:  
```bash
./ports2.py 192.168.1.1
```

🛠 **Use Case:** If you need to scan **a large number of ports quickly**, use `ports2.py`. The speed difference is especially noticeable for **remote servers** where latency is a concern.  

---

### **4️⃣ vulnscan.py - Vulnerability Scanner**  
📌 **Purpose:** Checks **running services** on detected open ports for **known vulnerabilities**.  
🔧 **How It Works:**  
- Identifies **service versions** running on open ports.  
- Compares versions against a **vulnerability database** (could be `CVE` lists).  
- Reports **security risks** related to the detected services.  

#### **Run Command:**  
```bash
./vulnscan.py <target-ip>
```
Example:  
```bash
./vulnscan.py 192.168.1.1
```

🛠 **Use Case:** If you need to identify **potential security risks** on a server, use `vulnscan.py` after running a port scan.  

---

## **🔄 Example Workflow (Step-by-Step Guide)**  
**To perform a full scan on a target, follow these steps:**  

1️⃣ **Display the banner**  
```bash
./banner.py
```
2️⃣ **Scan open ports (fast multi-threaded scan)**  
```bash
./ports2.py 192.168.1.1
```
3️⃣ **Perform vulnerability analysis on open ports**  
```bash
./vulnscan.py 192.168.1.1
```

---

## **🛡️ Security Notes & Legal Disclaimer**  
⚠️ **Unauthorized scanning of networks without permission is illegal.**  
- Always obtain **explicit authorization** before scanning a system.  
- This tool is intended for **ethical hacking, security research, and learning purposes only**.  
- The developer is **not responsible** for any misuse of this tool.  

---

## **💡 Contributions & Improvements**  
🚀 Contributions are always welcome! If you’d like to improve the tool, follow these steps:  

1️⃣ **Fork the repository**  
2️⃣ **Create a feature branch** (`git checkout -b feature-name`)  
3️⃣ **Make your changes and commit** (`git commit -m "Description of changes"`)  
4️⃣ **Push to your fork** (`git push origin feature-name`)  
5️⃣ **Open a Pull Request**  

🔹 **Potential Improvements:**  
✅ Add **UDP scanning** support  
✅ Integrate **Nmap API** for detailed service detection  
✅ Implement **CVE database integration** for more accurate vulnerability checks  

---

## **📜 License**  
This project is licensed under the **MIT License**. See `LICENSE` for details.  

---