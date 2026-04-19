from flask import Flask, render_template
import random
import socket

app = Flask(__name__)

container_hostname = socket.gethostname()

# list of cat images
images = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHU3c3FjMzV0ZGcxc2M4aHllaTFqNmNnb3Vlc3Q0cjNnZHUyejFlMSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/bnl7xKaEXMLhI475je/giphy.gif"
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHU3c3FjMzV0ZGcxc2M4aHllaTFqNmNnb3Vlc3Q0cjNnZHUyejFlMSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/5QXWRp1CNGnMnZunC3/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dGV4cW53dDlzcTJjaHlsbXpsOTcwa2oyc3BrbDJoZ215b3ZmOW03cyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/yvoFq8QV30ZZhVzMrR/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dGV4cW53dDlzcTJjaHlsbXpsOTcwa2oyc3BrbDJoZ215b3ZmOW03cyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/AQpUsaKCRD9gA/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dGV4cW53dDlzcTJjaHlsbXpsOTcwa2oyc3BrbDJoZ215b3ZmOW03cyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/kc1qe57aesZgI/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MTc4aWJvajZzenprc2xjOWx0ZTlkdzZkbzl1bGRqMmJmbXA2ZjcxOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/MngEsCTQcZRW8/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Njg4c293MjNrOHJ3d3BtYzZ4cGk5cDBoaG15emVhYnM3MTh6OHlmcCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/IJOu30pvxcR4A/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHU3c3FjMzV0ZGcxc2M4aHllaTFqNmNnb3Vlc3Q0cjNnZHUyejFlMSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/12gDWD2kgBTFnO/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MTc4aWJvajZzenprc2xjOWx0ZTlkdzZkbzl1bGRqMmJmbXA2ZjcxOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/3oKIPkHVR1luJjgAyA/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MXZlYTJsbWtjZnEwMnZ0cmk0dTkxaXh5eXFhOXN5eHJlYm9vNHExcCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/L31YRVxfExs0U/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3OHh1d2M4N2docG5iYjI3cTQ2MDlkZXNuZWp1Z2djOXJlZmxtYzE5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/55gGTev7s29mMr1ZNk/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MTc4aWJvajZzenprc2xjOWx0ZTlkdzZkbzl1bGRqMmJmbXA2ZjcxOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/G1SuUoS0Fgskpx1jHZ/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3M2JwYmxoOTU5Y295N3J6OHYxbjlkOHJ3c2Z4N3VmdDBtbWk0NmhocCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hL49uM9RwRpekdr52M/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NmY3MW51eGZzbzA4djR2MmxleXg5aWtzcm5mOHZvcGxqYzRnc3ZwbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/H1zIfgQFWJR82Et8Uw/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, hostname=container_hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
