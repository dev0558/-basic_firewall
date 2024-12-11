import tkinter as tk
from tkinter import messagebox
import random
import json
from datetime import datetime

RULES_FILE = "rules.json"
LOG_FILE = "traffic.log"

def load_firewall_rules():
    try:
        with open(RULES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_firewall_rules(rules):
    with open(RULES_FILE, "w") as file:
        json.dump(rules, file, indent=4)

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    return rules.get(ip, "allow")

def log_traffic(ip, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - IP: {ip}, Action: {action}\n")

def display_rules():
    rules = load_firewall_rules()
    rules_text.delete(1.0, tk.END)
    for ip, action in rules.items():
        rules_text.insert(tk.END, f"{ip}: {action}\n")

def add_rule():
    ip = ip_entry.get().strip()
    action = action_var.get()
    if not ip:
        messagebox.showwarning("Input Error", "IP address cannot be empty.")
        return
    rules = load_firewall_rules()
    rules[ip] = action
    save_firewall_rules(rules)
    display_rules()
    messagebox.showinfo("Success", f"Rule added: {ip} -> {action}")

def simulate_traffic():
    ip = generate_random_ip()
    rules = load_firewall_rules()
    action = check_firewall_rules(ip, rules)
    log_traffic(ip, action)
    traffic_label.config(text=f"Simulated IP: {ip}, Action: {action}")

# GUI Setup
root = tk.Tk()
root.title("Basic Firewall Simulation")

frame = tk.Frame(root)
frame.pack(pady=10)

rules_label = tk.Label(frame, text="Firewall Rules:")
rules_label.grid(row=0, column=0, padx=5, sticky="w")

rules_text = tk.Text(frame, width=40, height=10, wrap=tk.WORD, state="normal")
rules_text.grid(row=1, column=0, padx=5, pady=5)
display_rules()

ip_label = tk.Label(frame, text="IP Address:")
ip_label.grid(row=2, column=0, sticky="w", padx=5)
ip_entry = tk.Entry(frame, width=15)
ip_entry.grid(row=2, column=0, padx=90, sticky="w")

action_label = tk.Label(frame, text="Action:")
action_label.grid(row=3, column=0, sticky="w", padx=5)
action_var = tk.StringVar(value="allow")
action_dropdown = tk.OptionMenu(frame, action_var, "allow", "block")
action_dropdown.grid(row=3, column=0, padx=90, sticky="w")

add_button = tk.Button(frame, text="Add Rule", command=add_rule)
add_button.grid(row=4, column=0, pady=5)

traffic_button = tk.Button(root, text="Simulate Traffic", command=simulate_traffic)
traffic_button.pack(pady=5)
traffic_label = tk.Label(root, text="")
traffic_label.pack(pady=5)

root.mainloop()
