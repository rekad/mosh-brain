from flask import Flask, render_template
from gopigo import *
from subprocess import call

LEFT, RIGHT, FORWARD, BACK, STOP, TALK  = "left", "right", "forward", "back", "stop", "talk"
AVAILABLE_COMMANDS = {
    'Left': LEFT,
    'Right': RIGHT,
    'Forward': FORWARD,
    'Back': BACK,
    'Stop': STOP,
    'Talk': TALK
}


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html', commands=AVAILABLE_COMMANDS)


@app.route('/<cmd>')
def command(cmd=None):    
    camera_command = cmd[0].upper()
    response = "Moving {}".format(cmd.capitalize())
    print "Command: " + camera_command
    # GIVE GOPIGO COMMAND
    if camera_command == 'F':
        print "Moving forward"
        fwd()
    elif camera_command == 'B':
        bwd()
        print "Moving backward"
    elif camera_command == 'L':
        left()
        print "Turning left"
    elif camera_command == 'R':
        right()
        print "Turning right"
    elif camera_command == 'S':
        stop()
        print "Stopping"
    elif camera_command == 'T':
	print "Talking"
	call(["espeak","-s140","Hello everybody. Please cuddle me."])

    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=8080, debug=True)
