import socket

def handle_request(request):
    resources = {
        "ambulance": "Ambulance dispatched",
        "medivac": "Medivac unit dispatched",
        "firefighting": "Firefighting unit dispatched",
        "backup": "Backup dispatched",
        "more_assistance": "More assistance dispatched",
        "no_assistance": "No further assistance needed"
    }
    return resources.get(request, "Invalid request")

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("TCP Server: Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        response = handle_request(request)
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    tcp_server()
