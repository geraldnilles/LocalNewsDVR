
import os
from flask import Flask
from flask import render_template
from flask import send_from_directory

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    @app.route('/html')
    def main():
        recordings = ["05/31","06/01"] 
        return render_template('main.html', shows=recordings )

    @app.route('/video/<path:filename>')
    def library(filename):
        return send_from_directory("/tmp/localnews",filename)

    return app



