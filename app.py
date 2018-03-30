from flask import Flask, make_response

app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
	response = make_response(open("./public/index.html").read())
	return response

if (__name__ == "__main__"):
	app.run()