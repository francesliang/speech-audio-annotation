import os
import base64
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

from api.audio_handler import split_audio_to_files
from audio.utils import read_wave
from models.infer import infer_audio_file
from annotations.deep_speech import DeepSpeechAnnotation, DeepSpeechLabel
import config as cfg


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return


@app.route('/upload', methods=['POST'])
def upload_audio_file():
    if request.method == 'POST':
        f = request.files['file']
        file_path = os.path.join(cfg.clip_output_path, f.filename)
        f.save(file_path)
        audio_clips = split_audio_to_files(file_path) #TODO handle audio bytes directly
        return jsonify(audio_clips), 200


@app.route('/infer', methods=['POST'])
def run_inference():
    if request.method == 'POST':
        audio_clip = request.json['audio_clip']
        audio_path = os.path.join(cfg.clip_output_path, audio_clip)
        result = infer_audio_file(audio_path)
        return jsonify(result), 200


@app.route('/annotate', methods=['POST'])
def annotate():
    if request.method == 'POST':
        # TODO Update annotation_out and annotation_obj
        annotation_out = "annotation.csv"
        annotation_obj = DeepSpeechAnnotation()
        audio_id = request.json['clip_id']
        audio_file_name = request.json['clip_name']
        annotation = request.json['annotation']
        label = DeepSpeechLabel(audio_id, audio_file_name, annotation)
        annotation_obj.format_output(label)
        annotation_obj.write_output(annotation_out)
        return jsonify({"annotation_output": annotation_out}), 200


@app.route('/get_audio/<clip_name>', methods=['GET'])
def retrieve_audio(clip_name):
    clip_path = os.path.join(cfg.clip_output_path, clip_name)
    audio_data = open(clip_path, 'rb').read()
    return Response(audio_data, mimetype="audio/x-wav")


@app.route('/get_audio_clips/<file_name>', methods=['GET'])
def retrieve_audio_list(file_name):
    file_base, ext = os.path.basename(file_name).split('.')
    clips = [f for f in os.listdir(cfg.clip_output_path) if f.startswith(file_base)]
    return jsonify(clips), 200


