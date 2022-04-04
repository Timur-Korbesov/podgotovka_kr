from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    slovar = [
    {"locality": "Hooper Bay",
     "wind": "N",
     "speed": 2},
    {"locality": "Ambler",
     "wind": "NW",
     "speed": 5},
    {"locality": "Anderson",
     "wind": "SSW",
     "speed": 2},
    {"locality": "Ketchikan",
     "wind": "W",
     "speed": 0}
]
    return jsonify(slovar)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')