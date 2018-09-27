from flask import Flask, render_template, request, jsonify
from settings import Settings
from process_handlers.timelapse_handler import TimelapseHandler

app = Flask(__name__)

timelapse_handler = TimelapseHandler()
settings = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global timelapse_handler
    global settings

    if request.method == 'POST':
        settings = Settings(request.form)

        timelapse_handler.start(settings.count, settings.duration, settings.spacing)

    return render_template('index.html', settings=settings, is_running=timelapse_handler.is_running())

@app.route('/progress', methods=['GET'])
def progress():
    pass