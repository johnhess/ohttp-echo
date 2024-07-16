from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def echo():
    data = request.get_data(as_text=True)
    return f'You said {data}'

@app.route('/', methods=['GET'])
def info():
    return """
    This is a toy app that echos POST requests to /.<br/><br/>  
    Use /gateway as the OHTTP gateway endpoint."""

if __name__ == '__main__':
    app.run(debug=True)