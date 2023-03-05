from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fbranch1')
def fbranch1():
    return render_template('fbranch1.html')

if __name__=="__main__":
    app.run(debug=True)