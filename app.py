from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Hello from Flask and Docker'


if __name__ == "__main__":
    app.run(debug=True)