from flask import Flask, render_template, request
from settings import ExposureSettings
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    settings = None

    print(request.form)

    if request.method == 'POST':
        settings = ExposureSettings(request.form)
    
    print(settings)

    return render_template('index.html', settings=settings)