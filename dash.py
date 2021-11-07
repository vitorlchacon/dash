from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '<h1>Dashboard</h1>'

app.run()