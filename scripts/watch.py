#!/usr/bin/env python3

import time
import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)

#chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Bedroom TV"])
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Living Room TV"])

cast = chromecasts[0]
cast.wait()
print(cast)

mc = cast.media_controller
mc.play_media('http://10.0.0.217:8082/video/out.m3u8', 'application/x-mpegURL')
mc.block_until_active()

# mc.pause()
time.sleep(5)
mc.seek(0)
mc.play()

# Shut down discovery
pychromecast.discovery.stop_discovery(browser)

