from flask import Flask, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__, static_folder="public", static_url_path="")
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

@app.route("/")
def index():
	return send_from_directory("public", "index.html")

if (__name__ == "__main__"):
	socketio.run(app)