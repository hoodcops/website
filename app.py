from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/subscribe", methods=["POST"])
def process_subscription():
    pass
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)