import socket

def udp_client(alert_message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(alert_message.encode('utf-8'), ('localhost', 9090))
    client_socket.close()

if __name__ == "__main__":
    alert_message = input("Enter alert message: ")
    udp_client(alert_message)
