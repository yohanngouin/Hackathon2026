from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_points = []  # store heatmap points

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    
    # expected: {lat, lng, signal}
    data_points.append(data)

    return jsonify({"status": "success"})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data_points)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)