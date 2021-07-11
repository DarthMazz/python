from bottle import Bottle, template, static_file, redirect
from datetime import datetime as dt
import os


app = Bottle()


@app.route("/")
def index():
    return template("download")


@app.route('/searchdownload')
def searchdownload():
    return redirect('/download/abc.csv')


@app.route('/download/<file_path:path>')
def download(file_path):
    return static_file(file_path, root='./download', download=True)


def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)


if __name__ == '__main__':
    main()