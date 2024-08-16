import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.publish("test/topic", payload="Hello from MQTT Publisher!", qos=0, retain=False)

def mqtt_publisher():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    mqtt_publisher()
