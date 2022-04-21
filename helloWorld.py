from flask import Flask
from config import Config

app = Flask(__name__)
port = Config.port


@app.route('/', methods=['GET'])
def index():
    return "Hello to the World, this is your captain speaking. Masks ARE required on this flight."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=False)