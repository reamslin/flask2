from flask import Flask, render_template, request, jsonify
from helpers import *

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=['POST'])
def processPost():
    """On valid input data, returns JSON with a fact about a random number, and fact about their birth year
        Returns error JSON object if invalid input """
        
    result = getData(request.json)

    if result.msg == 'ok':
        return jsonify(result.value)
    else:
        return jsonify(errors=result.value)
