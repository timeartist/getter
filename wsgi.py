from json import loads, dumps

from flask import Flask, render_template
from redis import Redis

application = Flask(__name__)
redis = Redis(host="demo-db.redis1.svc.cluster.local", port=12345)

@application.route('/')
def show():
    return render_template('display.html')

@application.route('/data')
def data():
    return dumps(redis.lrange('form-inputs', 0, -1))

if __name__ == "__main__":
    application.run()
