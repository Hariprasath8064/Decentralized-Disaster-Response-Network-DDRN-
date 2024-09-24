import socket
import folium
from folium.plugins import HeatMap
import time

# Initialize map centered on a specific disaster location
map_center = folium.Map(location=[28.6139, 77.2090], zoom_start=14)  # Example: New Delhi

# Store beacon data
beacon_data = []

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
            temperature = float(parts[2].split(": ")[1].replace("C", ""))
            hazard_level = parts[3].split(": ")[1]

            # Add beacon data with intensity based on hazard level
            intensity = {"low": 0.2, "moderate": 0.5, "high": 1.0}.get(hazard_level, 0.1)
            beacon_data.append([lat, lon, intensity])

            # Update the map with the new data
            update_map(lat, lon, temperature, hazard_level, intensity)

        except Exception as e:
            print(f"Error processing message: {e}")

def update_map(lat, lon, temperature, hazard_level, intensity):
    # Update heatmap
    heatmap_layer = HeatMap(beacon_data, radius=20, max_zoom=14).add_to(map_center)

    # Create a marker for additional details on hover
    folium.Marker(
        location=[lat, lon],
        popup=f"Temp: {temperature}°C, Hazard: {hazard_level}",
        icon=folium.Icon(color="red" if hazard_level == "high" else "orange" if hazard_level == "moderate" else "green")
    ).add_to(map_center)

    # Save the updated map
    map_center.save("disaster_heatmap.html")
    print("Map updated!")

if __name__ == "__main__":
    udp_server()
