import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9090))
    print("UDP Server: Waiting for alerts...")

    while True:
        message, addr = server_socket.recvfrom(1024)
        print(f"Alert received from {addr}: {message.decode('utf-8')}")

if __name__ == "__main__":
    udp_server()
