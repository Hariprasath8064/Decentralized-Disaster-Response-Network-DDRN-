import socket

def udp_client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"Hello from UDP Client!", (server_ip, 8081))
    response, addr = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode()}")

if __name__ == "__main__":
    server_ip = "Enter_Server_IP_Here"
    udp_client(server_ip)
