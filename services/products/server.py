from flask import Flask
import os

app = Flask('Users')

@app.route("/")
def hello_world():
    return "<p>Products!</p>"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=os.getenv("SERVICE_PORT"))