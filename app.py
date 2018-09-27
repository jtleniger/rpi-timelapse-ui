from flask import Flask, render_template, request, jsonify
from settings import Settings
from process_handlers.timelapse_handler import TimelapseHandler

app = Flask(__name__)

timelapse_handler = TimelapseHandler()

@app.route('/', methods=['GET', 'POST'])
def index():
    global timelapse_handler
    settings = None

    if request.method == 'POST':
        settings = Settings(request.form)

        timelapse_handler.start(settings.count, settings.duration, settings.spacing)

    return render_template('index.html', settings=settings, status=timelapse_handler.status())

@app.route('/progress', methods=['GET'])
def progress():
    global timelapse_handler

    return jsonify({'progress': timelapse_handler.count_done()})