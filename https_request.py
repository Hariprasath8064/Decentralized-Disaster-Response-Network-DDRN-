import requests

def https_request():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

if __name__ == "__main__":
    https_request()
