# basic_firewall


# **Basic Firewall Project**

A Python-based simulation of a rule-based firewall designed to monitor and control network traffic. This project includes both a **command-line interface (CLI)** and a **graphical user interface (GUI)** for rule management, along with traffic logging and analytics.
Check this video to See the demonstration: https://youtu.be/SD6IPPylr8w

---

## **Features**
- **Rule-Based Access Control**: Blocks or allows traffic based on predefined rules stored in a JSON file.
- **Traffic Simulation**: Generates random traffic to test firewall behavior.
- **Logging**: Records all actions (block/allow) in a log file for auditing purposes.
- **GUI Management**: Provides a user-friendly interface for visualizing and managing rules.
- **Extensibility**: Modular design supports future enhancements like wildcard rules and real-time traffic monitoring.

---

## **Directory Structure**
```
basic_firewall/
├── firewall.py          # Main script for console-based simulation
├── firewall_gui.py      # GUI version of the firewall
├── rules.json           # JSON file to store firewall rules
├── traffic.log          # Log file for traffic actions (auto-created)
└── traffic_generator.py # Optional traffic generation module
```

### **File Descriptions**
1. **`firewall.py`**: Enforces firewall rules and logs actions.
2. **`firewall_gui.py`**: Provides a graphical interface for managing rules.
3. **`rules.json`**: Stores firewall rules in a structured format.
4. **`traffic.log`**: Captures details of all traffic actions for auditing.
5. **`traffic_generator.py`**: Simulates random traffic for testing purposes.

---

## **How It Works**
### **Firewall Rules**
Rules are stored in `rules.json` and define actions for specific IP addresses:
```json
{
    "192.168.1.1": "block",
    "192.168.1.4": "block",
    "192.168.1.9": "block",
    "192.168.1.13": "block",
    "192.168.1.16": "block",
    "192.168.1.19": "block"
}
```

- **Key**: Represents the IP address.
- **Value**: Specifies the action (`block` or `allow`).

### **Logging**
Traffic actions are logged in `traffic.log` with details like timestamps, IP addresses, and actions:
```
2024-12-07 00:42:25 - IP: 192.168.1.19, Action: block
2024-12-07 00:42:25 - IP: 192.168.1.8, Action: allow
```

---

## **Setup and Installation**
### **Pre-Requisites**
- **Python Version**: Python 3.6 or higher.
- **Libraries**: `tkinter` (default in most Python installations), `matplotlib` (for analytics).

### **Steps**
1. Clone or download the repository:
   ```bash
   git clone https://github.com/dev0558/basic_firewall.git
   cd basic_firewall
   ```
2. Install required dependencies:
   ```bash
   pip install matplotlib
   ```
3. (Optional) Set up a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Linux/Mac
   env\Scripts\activate     # On Windows
   ```

---

## **Usage**
### **1. Run the Console-Based Firewall**
Execute the script to simulate traffic:
```bash
python3 firewall.py
```

### **2. Launch the GUI**
Start the graphical user interface:
```bash
python3 firewall_gui.py
```

### **3. Simulate Traffic**
Generate random traffic for testing:
```bash
python3 traffic_generator.py
```

### **4. View Logs**
Inspect traffic logs for recorded actions:
```bash
cat traffic.log
```

---

## **Observations**
- Accurately enforces predefined rules.
- Provides intuitive GUI for rule management.
- Logs ensure traceability and transparency.

---

## **Challenges**
1. Ensuring immediate effect of rule changes in the GUI.
2. Handling larger rule sets or wildcard matching.
3. Optimizing GUI responsiveness for heavy traffic.

---

## **Future Enhancements**
1. Add **wildcard rule support** (e.g., `192.168.*`).
2. Integrate with **live traffic monitoring tools**.
3. Introduce **threat intelligence integration** for blocking malicious IPs.

---

## **Contributing**
Contributions are welcome! Please fork the repository and create a pull request for review.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

