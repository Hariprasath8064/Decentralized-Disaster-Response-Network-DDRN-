import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 8081))
    print("UDP Server listening on port 8081...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received: {data.decode()} from {addr}")
        server_socket.sendto(b"Data received", addr)

if __name__ == "__main__":
    udp_server()
