# -*- coding: utf-8 -*-

from flask import Flask
from flask import Response
from flask import stream_with_context

import requests

application = Flask(__name__)

@application.route('/<path:url>')
def home(url):
    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

@application.route("/")
def hello():
    return "Hello World! This is a Flask Proxy!"

if __name__ == "__main__":
    application.run()
