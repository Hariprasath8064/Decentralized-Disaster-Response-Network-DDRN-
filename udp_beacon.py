import socket
import time
import random


def udp_beacon():
    beacon_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_address = ('<broadcast>', 9090)
    beacon_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        # Simulate beacon hazard data (e.g., hazard level, temperature)
        beacon_id = random.randint(1000, 9999)
        hazard_data = {
            "beacon_id": beacon_id,
            "hazard_level": random.randint(1, 10),  # 1-10 hazard scale
            "temperature": random.uniform(20.0, 100.0)  # random temp in Celsius
        }
        message = f"Beacon {beacon_id} | Hazard: {hazard_data['hazard_level']} | Temp: {hazard_data['temperature']:.2f}C"
        beacon_socket.sendto(message.encode('utf-8'), broadcast_address)
        print(f"Broadcasting: {message}")

        time.sleep(5)  # Broadcast every 5 seconds


if __name__ == "__main__":
    udp_beacon()
