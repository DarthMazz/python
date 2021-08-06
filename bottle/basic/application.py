from bottle import Bottle, template, static_file
import os


app = Bottle()


@app.route('/main')
def main():
    return template('main')


@app.route('/<filepath>')
def root(filepath):
    return static_file(filepath, root="./")


@app.route("/img/<filepath>")
def images(filepath):
    return static_file(filepath, root="./img")


app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)
