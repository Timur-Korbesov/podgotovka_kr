from flask import Flask

app = Flask(__name__)


js = {
     "France": [
         {
             "size": 10,
             "fast": 2
         }
     ],
     "Sweden": [
         {
             "color": "rose"
         }
     ]
 }


@app.route('/')
def get_json():
    return js


if __name__ == '__main__':
    app.run()