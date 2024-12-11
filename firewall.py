import random
import json
from datetime import datetime

RULES_FILE = "rules.json"
LOG_FILE = "traffic.log"

def generate_random_ip():
    """Generate a random IP address."""
    return f"192.168.1.{random.randint(0, 20)}"

def load_firewall_rules():
    """Load firewall rules from a JSON file."""
    try:
        with open(RULES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_firewall_rules(rules):
    """Save firewall rules to a JSON file."""
    with open(RULES_FILE, "w") as file:
        json.dump(rules, file, indent=4)

def check_firewall_rules(ip, rules):
    """Check if the IP matches any rule and return the action."""
    return rules.get(ip, "allow")

def log_traffic(ip, action):
    """Log the IP traffic and action to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - IP: {ip}, Action: {action}\n")

def main():
    # Load firewall rules
    rules = load_firewall_rules()

    # Simulate random traffic
    print("Simulating network traffic...")
    for _ in range(12):
        ip = generate_random_ip()
        action = check_firewall_rules(ip, rules)
        log_traffic(ip, action)
        print(f"IP: {ip}, Action: {action}")

if __name__ == "__main__":
    main()
