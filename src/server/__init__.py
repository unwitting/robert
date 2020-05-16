from flask import Flask, render_template, request
import json

app = Flask(__name__)
robot = None

def start(r):
  app.run()
  robot = r

@app.route('/')
def robert():
  return render_template('robert.html')


@app.route('/dance', methods=['POST'])
def dance():
  return json.dumps('done')

@app.route('/move', methods=['POST'])
def move():
  direction = request.json['direction']
  return json.dumps(direction)