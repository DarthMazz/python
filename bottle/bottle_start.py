from bottle import Bottle, template, static_file
import os

# BASIC認証のユーザ名とパスワード
USERNAME = "user"
PASSWORD = "pass"


def check(username, password):
    u"""
    BASIC認証のユーザ名とパスワードをチェック
    @bottle.auth_basic(check)で適用
    """
    return username == USERNAME and password == PASSWORD


app = Bottle()

texts = [
    ""
    ,
    """
    素敵なシャネルのバッグです。シャネルのバッグは数十万円から百万円以上の値段で取引されており、その人気が伺える商品になっております。\nなんて
    素敵なんだろう。いやー素晴らしい。\nこんな素晴らしいものがこの世にあるだろうか？いやない。あるはずがない。なぜならシャネルだから。シャネルは素晴らしい。なんて素晴らしいのだろう
    そう思いませんか？"""
    ,
    """
    すっご〜〜い！インスタグラムのパクリが作れるフレンドなんだね！
    """
    ,
    """
    そら　きれい
    """
]


@app.get("/<username>")
def userpage(username):
    nums = [1, 2, 3]
    images = [(p1, p2) for p1, p2 in zip(nums, texts)]
    print(images)
    return template("userpage", username=username, texts=texts, images=images)


@app.route("/")
def index():
    return "<h1> hello my website!</h1>"


@app.route("/img/<filepath>")
def imgs(filepath):
    return static_file(filepath, root="./img")


@app.route("/pdf/<filepath>")
def pdfs(filepath):
    return static_file(filepath, root="./pdf", download=True)


app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), reloader=True, debug=True)
