from flask import Flask, render_template, request
# from gopigo import *
from subprocess import call
import time

LEFT, RIGHT, FORWARD, BACK, STOP, TALK  = "left", "right", "forward", "back", "stop", "talk"
AVAILABLE_COMMANDS = {
    'Left': LEFT,
    'Right': RIGHT,
    'Forward': FORWARD,
    'Back': BACK,
    'Stop': STOP,
    'Talk': TALK
}

# Sleep interval after moving
STIME_MOV = 2
# Sleep interval after rotation
STIME_ROT = 0.3

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html', commands=AVAILABLE_COMMANDS)

@app.route('/cmd/<cmd>')
def command(cmd=None):    
    camera_command = cmd[0].upper()
    response = "Performing Command: {}".format(cmd.capitalize())
    print "Command: " + camera_command
    # GIVE GOPIGO COMMAND
    if camera_command == 'F':
        print "Moving forward"
        # fwd()
        time.sleep(STIME_MOV)
        # stop()
    elif camera_command == 'B':
        # bwd()
        print "Moving backward"
        time.sleep(STIME_MOV)
        # stop()
    elif camera_command == 'L':
        # left()
        print "Turning left"
        time.sleep(STIME_ROT)
        # stop()
    elif camera_command == 'R':
        # right()
        print "Turning right"
        time.sleep(STIME_ROT)
        # stop()
    elif camera_command == 'S':
        # stop()
        print "Stopping"
    elif camera_command == 'T':
	print "Talking"
    # TODO: Validate msg 
	call(["espeak","-vde", "-s110",request.args.get('msg')])
    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=8080, debug=True)
