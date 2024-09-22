import socket
import uuid
import platform
import os
import speech_recognition as sr  # For voice commands
import pyttsx3
import time


def speak_text(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    # Say the text three times
    for _ in range(1):
        engine.say(text)
        engine.runAndWait()


# Function to fetch client information (e.g., MAC address or hostname)
def get_client_info():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                            for elements in range(0, 2 * 6, 8)][::-1])
    hostname = platform.node()  # Get the hostname of the client
    return f"Client: {hostname}, MAC: {mac_address}"


# Function to capture voice input
def capture_voice_request():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say your request:")
        audio = recognizer.listen(source)

        try:
            request = recognizer.recognize_google(audio)
            print(f"You said: {request}")
            return request
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your request.")
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
    return "invalid"  # Default request if voice recognition fails


def tcp_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))  # Connect to server

    # Automatically gather client info
    client_info = get_client_info()

    # Capture the user's voice request
    request = capture_voice_request()

    # Combine client info and request
    message = f"{client_info}, Request: {request}"
    message_size = len(message.encode('utf-8'))  # Calculate message size in bytes

    # Start timer for measuring response time
    start_time = time.time()

    # Send message to server
    client_socket.send(message.encode('utf-8'))

    # Receive response from the server
    response = client_socket.recv(1024).decode('utf-8')
    response_size = len(response.encode('utf-8'))  # Size of the response in bytes

    # Stop timer after receiving response
    end_time = time.time()

    # Calculate response time (round-trip time) in milliseconds
    response_time = (end_time - start_time) * 1000  # Response time in ms

    # Print and speak the server's response
    print(f"Response from server: {response}")
    speak_text(response)

    # Calculate throughput (in bits per second)
    total_data_size = message_size + response_size  # Total data in bytes
    time_taken = end_time - start_time  # Time taken for the round trip in seconds
    if time_taken > 0:
        throughput = (total_data_size * 8) / time_taken  # Convert bytes to bits and divide by time in seconds
    else:
        throughput = 0.0

    # Packet loss simulation (This assumes 1 packet sent and 1 received; adjust for real packet tracking)
    packets_sent = 1  # Simulating one request packet sent
    packets_received = 1 if response else 0  # Assume response received means packet was successful
    packet_loss = ((packets_sent - packets_received) / packets_sent) * 100  # Packet loss percentage

    # Latency approximation (since we don't have server-side timestamping, this will be half the round-trip time)
    latency = response_time / 2  # Half of the round-trip time



    # Write metrics to a file
    file_path = "performance_log.txt"
    log_entry = (
        f"Client Info: {client_info}\nRequest: {request}\nResponse: {response}\n"
        f"Latency: {latency:.2f} ms\nThroughput: {throughput / 1_000_000:.2f} Mbps\n"
        f"Packet Loss: {packet_loss:.2f}%\nResponse Time: {response_time:.2f} ms\n\n"
    )

    # Write performance metrics to the log file
    with open(file_path, 'a') as file:
        file.write(log_entry)

    # Close the socket
    client_socket.close()



if __name__ == "__main__":
    tcp_client()
