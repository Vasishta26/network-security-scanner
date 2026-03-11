import socket
import threading

print("==== Python Advanced Port Scanner ====\n")

target = input("Enter target IP or domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}\n")

lock = threading.Lock()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Unknown Service"

            with lock:
                print(f"[OPEN] Port {port} | Service: {banner}")

        s.close()

    except:
        pass


threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan complete.")