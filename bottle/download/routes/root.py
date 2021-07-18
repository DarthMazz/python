from bottle import Bottle, request, template


app = Bottle()


@app.route("/")
def index():
    print(get_remote_addr())
    return template("download")


def get_remote_addr():
    return request.remote_addr