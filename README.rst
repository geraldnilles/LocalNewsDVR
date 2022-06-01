################
 Local News DVR
################

This project will use the HDHomeRun connected to a digital antenna to capture
the local News every morning, store the file in RAM, and let me watch it at any
time that day.  The file will be overwritten each morning with today's news
cast.

This project will ahve 2 components: a transcode script and an web server

The Transcode script will run at a given time every day and save the local news
in an HLS format.  It will use the h264 hardware encoding block built into the
raspberry pi SoC.  It will use the HLS "Event" profile when transcoding so that
HLS streams start from the begining instead of start from **Live**. A systemd
timer will be used to kick-off this event at the right time.  I am not sure how
robust FFMPEG is to failures.  If the HDTV stream has a glitch or a TCP/IP
packet is dropped, will it power through or fail and need to be restarted? If
the latter, we might need to do a lower-level segmentation and write a separate
script that updates the playlist file

The web server will host the HLS video files (obviously), and it will also have
a very simple PyChromecast script that "kicks off" the stream. Using a full
python Flask appis probably overkill, but I can leverage my Episode player app
so its probably the easist path

