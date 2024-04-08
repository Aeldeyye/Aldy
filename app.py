from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/home-page")
def home():
    return "Hello And Welcome to My Web Services"

@app.route("/about-me-page")
def index():
    return "My Name Is Aldy ALfiansyah"

@app.route("/data")
def data():
    sample_data = {"Name" : "Aldy", "Age" : 20, "Class" : "LC01"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)

