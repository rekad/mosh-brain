#!/bin/sh
# launch_stream.sh
# Launch the mjpeg stream on startup

LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 30 -q 50 -x 640 -y 480 -vf" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &
