from flask import Flask, render_template, request, jsonify
from settings import Settings
from process_handlers.timelapse_handler import TimelapseHandler
from forms.run_timelapse import RunTimelapseForm

app = Flask(__name__)
app.secret_key = "developmentkey"

timelapse_handler = TimelapseHandler()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page. Form for triggering timelapses."""
    global timelapse_handler

    form = RunTimelapseForm()

    if form.validate_on_submit():
        timelapse_handler.start(form.count.data, form.duration.data, form.spacing.data)

    return render_template('index.html', form=form, is_running=timelapse_handler.is_running())

@app.route('/progress', methods=['GET'])
def progress():
    """Returns progress percentage as whole number in JSON."""

    global timelapse_handler

    print('in progress route')

    return jsonify({ 'progress': timelapse_handler.progress() })