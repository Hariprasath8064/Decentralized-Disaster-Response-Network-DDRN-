import socket
import folium
from folium.plugins import HeatMap
import time

# Initialize map centered on a specific disaster location
map_center = folium.Map(location=[28.6139, 77.2090], zoom_start=14)  # Example: New Delhi

# Store beacon data
beacon_data = {}


def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9090))
    print("UDP Server: Waiting for data from beacons...")

    while True:
        message, addr = server_socket.recvfrom(1024)
        data = message.decode('utf-8')
        print(f"Received: {data} from {addr}")

        # Parse the message
        try:
            parts = data.split(", ")
            lat = float(parts[0].split(": ")[1])
            lon = float(parts[1].split(": ")[1])
            temperature = parts[2].split(": ")[1]
            hazard_level = parts[3].split(": ")[1]

            # Update beacon data
            beacon_data[(lat, lon)] = (temperature, hazard_level)

            # Update the map
            update_map(lat, lon, temperature, hazard_level)

        except Exception as e:
            print(f"Error processing message: {e}")


def update_map(lat, lon, temperature, hazard_level):
    # Create a marker for the beacon
    color = {"low": "green", "moderate": "orange", "high": "red"}.get(hazard_level, "blue")

    folium.CircleMarker(
        location=[lat, lon],
        radius=10,
        popup=f"Temp: {temperature}, Hazard: {hazard_level}",
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7
    ).add_to(map_center)

    # Save the updated map
    map_center.save("disaster_map.html")
    print("Map updated!")


if __name__ == "__main__":
    udp_server()
