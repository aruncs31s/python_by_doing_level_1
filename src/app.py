from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def go_home():
    return "<h1>You are in home</h1>"

@app.route('/hello/<name>')
def hello_name(name: str):
    return f"<h1>Hello, {name}!</h1>"
    
@app.route('/<parameter_name>')
def function_name(parameter_name: str):
    return f"{eval(parameter_name)}"


if __name__ == "__main__":
    app.run(debug=True)