import os
import base64
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from models.infer import infer_audio_file


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return


@app.route('/infer', methods=['POST'])
def run_inference():
    if request.method == 'POST':
        audio_clip = request.json['audio_clip']
        audio_path = os.path.join(cfg.clip_output_path, audio_clip)
        result = infer_audio_file(audio_path)
        return jsonify(result), 200

