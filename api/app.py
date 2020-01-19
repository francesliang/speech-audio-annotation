from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return


@app.route('/upload', methods=['POST'])
def upload_audio_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        # TODO segment audio file


@app.route('/infer', methods=['POST'])
def run_inference():
    if request.method == 'POST':
        audio = request.form['audio']
        return


@app.route('/annotate', methods=['POST'])
def annotate():
    if request.method == 'POST':
        audio_file_name = request.form['clip_file_name']
        annotation = request.form['annotation']
        return


