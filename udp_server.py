import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9091))
    print("Server: Waiting for data from listeners...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode('utf-8')}")
        # Here, you'd map the data for analysis, e.g., hazard mapping visualization

if __name__ == "__main__":
    udp_server()
