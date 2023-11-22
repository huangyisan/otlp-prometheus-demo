# from flask import Flask
# from prometheus_flask_exporter import PrometheusMetrics

# app = Flask(__name__)
# metrics = PrometheusMetrics(app)

# @app.route('/')
# def main():
#     return 'OK'




import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)


endpoints = ("one", "two", "three", "four", "five", "error")


@app.route("/one")
def first_route():
    time.sleep(random.random() * 0.2)
    return "ok"


@app.route("/two")
def the_second():
    time.sleep(random.random() * 0.4)
    return "ok"


@app.route("/three")
def test_3rd():
    time.sleep(random.random() * 0.6)
    return "ok"


@app.route("/four")
def fourth_one():
    time.sleep(random.random() * 0.8)
    return "ok"


@app.route("/error")
def oops():
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)


# third
# """
# Package usage example

# Make sure `flask_prometheus_metrics` installed  first.
# Run script as follows:

# $ python example.py
# """
# from flask import Blueprint, Flask
# from prometheus_client import make_wsgi_app
# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from werkzeug.serving import run_simple
# from flask_prometheus_metrics import register_metrics

# #
# # Constants
# #

# CONFIG = {"version": "v0.1.2", "config": "staging"}
# MAIN = Blueprint("main", __name__)


# #
# # Main app
# #


# @MAIN.route("/")
# def index():
#     return "Test"


# def register_blueprints(app):
#     """
#     Register blueprints to the app
#     """
#     app.register_blueprint(MAIN)


# def create_app(config):
#     """
#     Application factory
#     """
#     app = Flask(__name__)

#     register_blueprints(app)
#     register_metrics(app, app_version=config["version"], app_config=config["config"])
#     return app


# #
# # Dispatcher
# #


# def create_dispatcher() -> DispatcherMiddleware:
#     """
#     App factory for dispatcher middleware managing multiple WSGI apps
#     """
#     main_app = create_app(config=CONFIG)
#     return DispatcherMiddleware(main_app.wsgi_app, {"/metrics": make_wsgi_app()})


# #
# # Run
# #

# if __name__ == "__main__":
#     run_simple(
#         "localhost",
#         5000,
#         create_dispatcher(),
#         use_reloader=True,
#         use_debugger=True,
#         use_evalex=True,
#     )