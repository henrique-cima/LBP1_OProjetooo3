from flask import Flask, render_template
from controlers import controller

app = Flask(__name__)

@app.route('/')
def index():
    data = Controller().index()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
