from flask import Flask

app = Flask(__name__)

@app.route('/api')
def api():
    return 'Hi, I\'m the API!'

if __name__ == '__main__':
    app.run(debug=True)
