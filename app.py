
from flask import Flask, request

app = Flask(__name__)
@app.route('/login',methods = ['POST', 'GET'])
def demo():
    return "<html><head><body>HELLO</body></head></html>"



if __name__ == "__main__":
    app.run(port=8080)
