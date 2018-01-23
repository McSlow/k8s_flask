import os

from flask import Flask
from redis import Redis

import socket
app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])


@app.route('/')
def hello_world():
    return '<H1 style="position:fixed; top: 50%; left:50%;transform: translate(-50%, -50%);">Hello from Docker Meetup Bamberg</H1>' + '<br>Container Hostname: ' + socket.gethostname() + '<br>I have been clicked {} times.'.format(redis.get('hits'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)