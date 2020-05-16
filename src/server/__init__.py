from flask import Flask, render_template, request
import json

app = Flask(__name__)
robot = None

def start(r):
  global robot
  robot = r
  app.run(host="0.0.0.0")

@app.route('/')
def robert():
  return render_template('robert.html')


@app.route('/dance', methods=['POST'])
def dance():
  robot.dance()
  return json.dumps('dance')

@app.route('/move', methods=['POST'])
def move():
  movements = {
    'forward': robot.begin_forward_move,
    'reverse': robot.begin_backward_move,
    'left': robot.begin_anticlockwise_turn,
    'right': robot.begin_clockwise_turn,
    'stop': robot.begin_brake,
  }
  direction = request.json['direction']
  movements[direction]()
  return json.dumps(direction)
