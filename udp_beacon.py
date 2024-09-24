import socket
import time
import random

def generate_beacon_data():
    temperature = random.uniform(20.0, 40.0)  # Temperature range in Celsius
    hazard_level = random.choice(['low', 'moderate', 'high'])  # Hazard levels
    return temperature, hazard_level

def udp_beacon(lat, lon):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 9090)  # UDP server address

    while True:
        temperature, hazard_level = generate_beacon_data()
        message = f"Lat: {lat}, Lon: {lon}, Temp: {temperature:.2f}C, Hazard: {hazard_level}"

        # Send data to the UDP server
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Wait before sending the next update (e.g., every 10 seconds)
        time.sleep(10)

if __name__ == "__main__":
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    udp_beacon(lat, lon)
