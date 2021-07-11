from bottle import Bottle, template, static_file, request, redirect
from datetime import datetime as dt
import os


app = Bottle()


@app.route("/")
def index():
    start = request.query.get('start')
    start = "0" if start is None else start
    print(start)
    return template("pagenation", hit_count=None, contents=None, start=start)


def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)


if __name__ == '__main__':
    main()