import paho.mqtt.client as mqtt

def mqtt_publisher(message):
    client = mqtt.Client()
    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    client.publish("ddrn/updates", message)
    client.disconnect()

if __name__ == "__main__":
    message = input("Enter message to publish: ")
    mqtt_publisher(message)
