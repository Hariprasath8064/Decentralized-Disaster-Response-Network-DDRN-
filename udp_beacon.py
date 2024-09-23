import socket
import time
import random


# Function to simulate beacon data (temperature, hazard levels)
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

        # Wait for some time before sending the next update (e.g., every 10 seconds)
        time.sleep(10)


if __name__ == "__main__":
    # Fixed coordinates for each beacon
    lat = float(input("Enter latitude: "))  # Specify lat for each beacon instance
    lon = float(input("Enter longitude: "))  # Specify lon for each beacon instance

    udp_beacon(lat, lon)
