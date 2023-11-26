import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run('127.0.0.1')