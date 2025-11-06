import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} is OPEN")
                else:
                    print(f"Port {port} is CLOSED")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# Example usage
target_host = "127.0.0.1"
target_ports = [21, 22, 80, 443]
scan_ports(target_host, target_ports)