import random

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"
