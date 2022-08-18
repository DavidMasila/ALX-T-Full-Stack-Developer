from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description':'todo 1'
    }, {
        'description':'todo 2'
    }, {
        'description':'todo 3'
    }])