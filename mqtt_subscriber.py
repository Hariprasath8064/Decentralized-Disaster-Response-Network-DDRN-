import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode('utf-8')}")

def mqtt_subscriber():
    client = mqtt.Client()
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    client.subscribe("ddrn/updates")
    client.loop_forever()

if __name__ == "__main__":
    mqtt_subscriber()
