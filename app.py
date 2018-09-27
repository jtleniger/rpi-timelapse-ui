from flask import Flask, render_template, request
from settings import Settings
from process_handlers.timelapse_handler import TimelapseHandler
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG)

app = Flask(__name__)

timelapse_handler = TimelapseHandler()

@app.route('/', methods=['GET', 'POST'])
def index():
    settings = None

    print(request.form)

    if request.method == 'POST':
        settings = Settings(request.form)

        timelapse_handler.start(settings.count, settings.duration, settings.spacing)

    return render_template('index.html', settings=settings, status=timelapse_handler.status())