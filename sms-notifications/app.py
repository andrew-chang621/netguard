from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_messages():
    """[SUMMARY]

    Returns:
        [RETURN TYPE] -- [DESC]
    """

    return jsonify(
            code="200",
            message="Hello, World.",)


@app.route("/", methods=["POST"])
def send_message():
    """[SUMMARY]

    Returns:
        [RETURN TYPE] -- [DESC]
    """

    return jsonify(
            code="200",
            message="Hello, World.",)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)