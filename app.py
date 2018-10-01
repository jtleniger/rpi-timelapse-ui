from flask import Flask, render_template, request, jsonify
from process_handlers.sequence_handler import SequenceHandler
from forms.run_sequence import RunSequenceForm

app = Flask(__name__)
app.secret_key = "developmentkey"

sequence_handler = SequenceHandler()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page. Form for triggering sequences."""
    global sequence_handler

    form = RunSequenceForm()

    if form.validate_on_submit():
        if form.start.data:
            sequence_handler.start(form.count.data, form.duration.data, form.spacing.data)
        if form.stop.data:
            sequence_handler.stop()

    return render_template('index.html', form=form, is_running=sequence_handler.is_running())

@app.route('/progress', methods=['GET'])
def progress():
    """Returns progress percentage as whole number in JSON."""

    global sequence_handler

    return jsonify({ 'progress': sequence_handler.progress() })