import os
from flask import Flask, request, jsonify

from api.audio_handler import split_audio_to_files
from audio.utils import read_wave
from models.infer import infer_audio
from annotations.deep_speech import DeepSpeechAnnotation, DeepSpeechLabel
import config as cfg


app = Flask(__name__)


@app.route('/')
def index():
    return


@app.route('/upload', methods=['POST'])
def upload_audio_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        audio_clips = split_audio_to_files(f.filename) #TODO handle audio bytes directly
        return jsonify(audio_clips), 200


@app.route('/infer', methods=['POST'])
def run_inference():
    if request.method == 'POST':
        audio = request.form['audio_data']
        sample_rate = request.form['sample_rate']
        result = infer_audio(audio, sample_rate)
        return jsonify(result), 200


@app.route('/annotate', methods=['POST'])
def annotate():
    if request.method == 'POST':
        # TODO Update annotation_out and annotation_obj
        annotation_out = "annotation.csv"
        annotation_obj = DeepSpeechAnnotation()
        audio_id = request.form('clip_id')
        audio_file_name = request.form['clip_file_name']
        annotation = request.form['annotation']
        label = DeepSpeechLabel(audio_id, audio_file_name, annotation)
        annotation_obj.format_output(label)
        annotation_obj.write_output(annotation_out)
        return jsonify({"annotation_output": annotation_out}), 200


@app.route('/get_audio/<clip_name>', methods=['GET'])
def retrieve_audio(clip_name):
    clip_path = os.path.join(cfg.clip_output_path, clip_name)
    audio_data, sample_rate, duration = read_wave(clip_path)
    return jsonify({
        "audio_data": audio_data,
        "sample_rate": sample_rate,
        "duration": duration
        }), 200




