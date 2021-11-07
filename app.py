from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('dashboard.html')

app.run()