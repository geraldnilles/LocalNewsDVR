
import os
import time
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


    @app.route('/play/<name>/<device>',methods=['GET'])
    def play(name,device):

        import pychromecast
        import socket

        services, browser = pychromecast.discovery.discover_chromecasts()
        pychromecast.discovery.stop_discovery(browser)

        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[device])

        cast = chromecasts[0]
        cast.wait()
        cast.quit_app()

        time.sleep(3)

        mc = cast.media_controller
        mc.play_media("http://"+socket.gethostname()+".lan:8082/video/"+name+"/out.m3u8", 'application/x-mpegURL')
        mc.block_until_active()

        # mc.pause()
        time.sleep(5)
        mc.seek(0)
        mc.play()

        # Shut down discovery
        pychromecast.discovery.stop_discovery(browser)
         
        return "Playing "+name+" on "+device

    return app



