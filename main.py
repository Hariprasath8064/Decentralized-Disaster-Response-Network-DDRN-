import threading
import tcp_server
import tcp_client
import udp_server
import udp_client
import https_request
import mqtt_publisher
import mqtt_subscriber
import blockchain


def start_tcp_server():
    tcp_server.tcp_server()


def start_tcp_client(server_ip):
    tcp_client.tcp_client(server_ip)


def start_udp_server():
    udp_server.udp_server()


def start_udp_client(server_ip):
    udp_client.udp_client(server_ip)


def start_https_request():
    https_request.https_request()


def start_mqtt_publisher():
    mqtt_publisher.mqtt_publisher()


def start_mqtt_subscriber():
    mqtt_subscriber.mqtt_subscriber()


def start_blockchain_logger():
    blockchain.blockchain()


if __name__ == "__main__":
    server_ip = "Enter_Server_IP_Here"

    # Threads for each module
    threads = []
    threads.append(threading.Thread(target=start_tcp_server))
    threads.append(threading.Thread(target=start_udp_server))
    threads.append(threading.Thread(target=start_https_request))
    threads.append(threading.Thread(target=start_mqtt_subscriber))
    threads.append(threading.Thread(target=start_blockchain_logger))

    # Start TCP Client and UDP Client on different devices
    threads.append(threading.Thread(target=start_tcp_client, args=(server_ip,)))
    threads.append(threading.Thread(target=start_udp_client, args=(server_ip,)))
    threads.append(threading.Thread(target=start_mqtt_publisher))

    # Start all threads
    for thread in threads:
        thread.start()

    # Join threads to ensure complete execution
    for thread in threads:
        thread.join()
