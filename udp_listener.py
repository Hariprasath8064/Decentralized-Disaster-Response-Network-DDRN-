import socket

def udp_listener():
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener_socket.bind(('localhost', 9090))
    server_address = ('localhost', 9091)

    print("Listener: Waiting for beacon broadcasts...")

    while True:
        message, addr = listener_socket.recvfrom(1024)
        print(f"Received from Beacon: {message.decode('utf-8')}")

        # Forward to central server
        listener_socket.sendto(message, server_address)
        print(f"Forwarded to server: {message.decode('utf-8')}")

if __name__ == "__main__":
    udp_listener()
