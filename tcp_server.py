import socket
import pyttsx3


def speak_text(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    # Say the text three times
    for _ in range(1):
        engine.say(text)
        engine.runAndWait()


def handle_request(client_info, request):
    print(f"Client Info: {client_info}")
    print(f"Request: {request}")

    resources = {
        "ambulance": "Ambulance dispatched",
        "medevac": "Medivac unit dispatched",
        "fire": "Firefighting unit dispatched",
        "backup": "Backup dispatched",
        "more assistance": "More assistance dispatched",
        "no assistance": "No further assistance needed",
        "God": "Ajithey !!"
    }

    # AI voice speaks out the request for the admin
    speak_text(f"Request from {client_info}: {request}")

    # Dispatch the response directly based on the client's request
    response = resources.get(request.lower(), "Invalid request")

    return response


def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("TCP Server: Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024).decode('utf-8')

        # Split client info and request
        client_info, request = data.split(", Request: ")
        print(f"Received request from {client_info}: {request}")

        # Handle the request and respond
        response = handle_request(client_info, request)
        client_socket.send(response.encode('utf-8'))
        client_socket.close()


if __name__ == "__main__":
    tcp_server()
