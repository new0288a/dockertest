from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell():
	return "hello world! This web service is installed on Docker."

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8888)
