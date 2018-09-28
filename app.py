from flask import Flask, render_template, request, jsonify
from settings import Settings
from process_handlers.timelapse_handler import TimelapseHandler
from forms.run_timelapse import RunTimelapseForm

app = Flask(__name__)
app.secret_key = "developmentkey"

# timelapse_handler = TimelapseHandler()
# settings = None

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page. Form for triggering timelapses."""
    form = RunTimelapseForm()


    # global timelapse_handler
    # global settings

    # if request.method == 'POST':
    #     settings = Settings(request.form)

    #     timelapse_handler.start(settings.count, settings.duration, settings.spacing)

    return render_template('index.html', form=form)

@app.route('/progress', methods=['GET'])
def progress():
    """TODO: return progress percentage as whole number in JSON."""
    pass