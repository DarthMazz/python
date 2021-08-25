import os
from routes import root
from routes import download
from routes.configs import Configs

app = root.app


def main():
    Configs.load('develop')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)


if __name__ == '__main__':
    main()