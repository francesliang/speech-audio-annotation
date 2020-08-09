import os
import base64
from flask import request, jsonify, Response
from flask_cors import CORS

from app.audio_handler import split_audio_to_files
from audio.utils import read_wave
from models.infer import infer_audio_file
from models.train import run_training
from annotations.deep_speech import DeepSpeechAnnotation, DeepSpeechLabel
from speech_recognition.google_stt import recognise
import config as cfg
from app import app


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


@app.route('/recognise', methods=['POST'])
def run_recognition():
    if request.method == 'POST':
        audio_clip = request.json['audio_clip']
        audio_path = os.path.join(cfg.clip_output_path, audio_clip)
        result = recognise(audio_path)
        return jsonify(result), 200


@app.route('/annotate', methods=['POST'])
def annotate():
    if request.method == 'POST':
        audio_id = request.json['clip_id']
        audio_file_name = request.json['clip_name']
        annotation = request.json['annotation']
        annotation_file = request.json.get('annotation_file', None)

        if annotation_file:
            annotation_out = os.path.join(cfg.annotation_output_path, annotation_file) + ".tsv"
        else:
            annotation_out = os.path.join(cfg.annotation_output_path, "annotations.tsv")
        annotation_obj = DeepSpeechAnnotation(annotation_file=annotation_out)

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


@app.route('/train', methods=['GET'])
def train_model():
    # TODO update train params
    run_training()
    return "OK", 200

