from flask import Flask, request, jsonify
from utils.func import getMatchingArticles
import json

app = Flask(__name__)
app.secret_key = "dljsaklqk24e21cjn!Ew@@dsa5"
response = ""

@app.route("/", methods=["GET"])
def home():

	return """<h1>Fake news detection</h1>
<p>A prototype API for detecting tweets containing fake news.</p>"""


@app.route("/api/v1", methods=["GET"])
def checkFake():

    global response
    
    if (request.method == "POST"):

        request_data = request.data
        request_data = json.loads(request_data.decode("utf-8"))
        url = request_data["url"]
        results = getMatchingArticles(url)
        response = jsonify(results)
        return " "

    else:

        return response
    

if (__name__ == "__main__"):

	app.run(debug = True)