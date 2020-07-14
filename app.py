from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/status')
def status():
    return 'Status: OK'


@app.route('/about')
def about():
    return 'About us'


@app.route('/contacts')
def contacts():
    return ' my contacts'


if __name__ == '__main__':
    app.run()
