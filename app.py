from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return {"message": "Hello from Flask!"}

if __name__ == "__main__":
    app.run(debug=True)

#prueba