from bottle import template, static_file, redirect
import os
from . import root

app = root.app


@app.route('/searchdownload')
def searchdownload():
    return redirect('/download/abc.csv')


@app.route('/download/<file_path:path>')
def download(file_path):
    return static_file(file_path, root='./download', download=True)