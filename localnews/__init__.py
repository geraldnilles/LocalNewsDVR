
import os
from flask import Flask
from flask import render_template
from flask import send_from_directory

from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

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
        recordings = [] 
        libpath = os.path.abspath( "/mnt/library" )
        for f in os.listdir( libpath ):
            if os.path.isdir( os.path.join( libpath,f ) ):
                recordings.append( f )
        return render_template('main.html', shows=recordings )

    @app.route('/video/<path:filename>')
    def library(filename):
        return send_from_directory("/mnt/library",filename, cache_timeout=0)

    return app



