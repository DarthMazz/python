from bottle import template, static_file, redirect
import os
from . import root
from .configs import Configs

app = root.app


@app.route('/searchdownload')
def searchdownload():
    print(Configs.test['application.run.host'])
    return redirect('/download/abc.csv')


@app.route('/download/<file_path:path>')
def download(file_path):
    return static_file(file_path, root='./download', download=True)