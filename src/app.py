from flask import Flask, jsonify
import json, datetime, socket


app = Flask(__name__)


@app.route('/api/v1/info')

def details():
    timeNow = datetime.date.today().strftime("%I:%Mp on %B %d, %Y")
    return jsonify({
        'time': timeNow,
        'hostname': socket.gethostname(),
        'message': "I love Marilyn Monroe!!!",
        'message2': "ICEMAN: AOTY!!!"
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status':'up'}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")

#'/api/v1/details'
#'/api/v1/healthz'
