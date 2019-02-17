from flask import Flask, jsonify, request
import remoteit
import authentication
import texting

# Initialize the Flask App
app = Flask(__name__)

# Add authentication middleware
app.wsgi_app = authentication.AuthenticationMiddleWare(app.wsgi_app)


@app.route("/", methods=["GET"])
def get_messages():
    """[SUMMARY]

    Returns:
        [RETURN TYPE] -- [DESC]
    """

    return jsonify(
        code="200",
        message=remoteit.get_ssh_url())


@app.route("/", methods=["POST"])
def send_message():
    """[SUMMARY]

    Returns:
        [RETURN TYPE] -- [DESC]
    """
    xf = request.get_json()
    texting.send_text("+17608778720", "+15012323138", xf["destination"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
