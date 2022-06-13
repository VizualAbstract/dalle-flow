from flask import Flask, request, jsonify
import sys
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
print("--> Starting DALL-E Server. This might take up to two minutes.")


@app.route("/", methods=["GET"])
@cross_origin()
def health_check():
    return jsonify(success=True)


with app.app_context():
    print("--> DALL-E Server is up and running!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(sys.argv[1]), debug=False)
