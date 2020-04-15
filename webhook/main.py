from flask import Flask, request
import json

app = Flask(__name__)
 
@app.route('/')
def hello():
    hello = "Hello world"
    return hello
 
@app.route('/webhook', methods=['POST'])
def webhook():
    print(json.loads(request.data))
    return 'Hello'
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8880)
