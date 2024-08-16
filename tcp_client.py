import socket

def tcp_client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 8080))
    client_socket.sendall(b"Hello from TCP Client!")
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")
    client_socket.close()

if __name__ == "__main__":
    server_ip = "Enter_Server_IP_Here"
    tcp_client(server_ip)
