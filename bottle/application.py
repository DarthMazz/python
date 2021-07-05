from bottle import Bottle, template, static_file, request
from datetime import datetime as dt
import os


app = Bottle()


@app.get("/search")
def search():
    # print(request.query.searchsort)
    contents = list()
    contents.append(
        {
            "image_path": "/img/1.jpg",
            "name": "aiueo",
            "order_number": "aiueo",
            "supplier_code": "aiueo",
            "attr_date.acceptance_date": "2018-01-02 03:04:05",
            "attr_date.order_date": "2018-01-02 03:04:05",
            "attr_string.product_name": "aiueo",
            "attr_string.model": "aiueo",
            "attr_string.maker_name": "aiueo",
        }
    )
    contents[0]['attr_date.acceptance_date.str'] = dt.strptime(contents[0]['attr_date.acceptance_date'], '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
    return template("application", hit_count=100, contents=contents)


@app.route("/")
def index():
    return template("application", hit_count=None, contents=None)


@app.route('/img/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./img')



def main():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)


if __name__ == '__main__':
    main()