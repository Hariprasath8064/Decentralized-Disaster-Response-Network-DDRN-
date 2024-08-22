import socket

def tcp_client(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    client_socket.send(request.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Response from server: {response}")
    client_socket.close()

if __name__ == "__main__":
    print("Select a resource to request:")
    print("1. ambulance\n2. medivac\n3. firefighting\n4. backup\n5. more_assistance\n6. no_assistance")
    choice = input("Enter your choice: ")
    requests = {
        "1": "ambulance",
        "2": "medivac",
        "3": "firefighting",
        "4": "backup",
        "5": "more_assistance",
        "6": "no_assistance"
    }
    request = requests.get(choice, "invalid")
    tcp_client(request)
