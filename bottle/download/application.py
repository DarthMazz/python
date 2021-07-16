from bottle import Bottle
import os
from routes import bottleapp
from routes import download


app = bottleapp.app


def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)


if __name__ == '__main__':
    main()