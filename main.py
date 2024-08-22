import threading
import tcp_server
import tcp_client
import udp_server
import udp_client
import https_request
import mqtt_publisher
import mqtt_subscriber

def start_tcp_server():
    tcp_server.tcp_server()

def start_tcp_client(server_ip):
    tcp_client.tcp_client(server_ip)

def start_udp_server():
    udp_server.udp_server()

def start_udp_client(server_ip):
    udp_client.udp_client(server_ip)

def start_https_request(location):
    https_request.fetch_geospatial_data(location)

def start_mqtt_publisher(message):
    mqtt_publisher.mqtt_publisher(message)

def start_mqtt_subscriber():
    mqtt_subscriber.mqtt_subscriber()

if __name__ == "__main__":
    server_ip = "localhost"

    # Menu for user to select the service they want to use
    print("Select the service(s) you want to use:")
    print("1. TCP")
    print("2. UDP")
    print("3. MQTT")
    print("4. HTTPS")
    print("5. All of the above")

    selected_services = input("Enter your choice (e.g., 1, 2, 3): ").strip().split(",")

    # Threads for the selected services
    threads = []

    if "1" in selected_services:
        threads.append(threading.Thread(target=start_tcp_server))
        threads.append(threading.Thread(target=start_tcp_client, args=(server_ip,)))

    if "2" in selected_services:
        threads.append(threading.Thread(target=start_udp_server))
        threads.append(threading.Thread(target=start_udp_client, args=(server_ip,)))

    if "3" in selected_services:
        mqtt_message = input("Enter the MQTT alert message to publish (or press Enter to skip): ").strip()
        if mqtt_message:
            threads.append(threading.Thread(target=start_mqtt_publisher, args=(mqtt_message,)))
        threads.append(threading.Thread(target=start_mqtt_subscriber))

    if "4" in selected_services:
        location = input("Enter the location for HTTPS request: ").strip()
        threads.append(threading.Thread(target=start_https_request, args=(location,)))

    if "5" in selected_services:
        # Start all services
        threads.append(threading.Thread(target=start_tcp_server))
        threads.append(threading.Thread(target=start_udp_server))
        location = input("Enter the location for HTTPS request: ").strip()
        threads.append(threading.Thread(target=start_https_request, args=(location,)))
        threads.append(threading.Thread(target=start_mqtt_subscriber))
        threads.append(threading.Thread(target=start_tcp_client, args=(server_ip,)))
        threads.append(threading.Thread(target=start_udp_client, args=(server_ip,)))
        mqtt_message = input("Enter the MQTT alert message to publish (or press Enter to skip): ").strip()
        if mqtt_message:
            threads.append(threading.Thread(target=start_mqtt_publisher, args=(mqtt_message,)))

    # Start all threads
    for thread in threads:
        thread.start()

    # Join threads to ensure complete execution
    for thread in threads:
        thread.join()
