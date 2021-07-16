from bottle import template, static_file, redirect
import os
from . import bottleapp

app = bottleapp.app

@app.route("/")
def index():
    return template("download")


@app.route('/searchdownload')
def searchdownload():
    return redirect('/download/abc.csv')


@app.route('/download/<file_path:path>')
def download(file_path):
    return static_file(file_path, root='./download', download=True)