from flask import Flask, render_template

# reference
# jinja2 template
# https://tanuhack.com/jinja2-block/
# https://tanuhack.com/jinja2-if-for/


app = Flask(__name__)

@app.route('/')
def route_route():
    test_list = ['1', '2', '3']
    return render_template('main.html', test_list=test_list)

def main():
    app.run(host='0.0.0.0', debug=False)

if __name__ == '__main__':
    main()
