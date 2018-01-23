from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<H1 style="position:fixed; top: 50%; left:50%;transform: translate(-50%, -50%);">Hello from Docker Meetup Bamberg</H1><br>Container Hostname: ' + socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)