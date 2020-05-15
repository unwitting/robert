from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def robert():
  return render_template('robert.html')