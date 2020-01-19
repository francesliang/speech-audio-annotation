import os
import sys
from typing import Dict
import logging
from collections import namedtuple
import numpy as np

import models.deepspeech.inference as ds
import models.deepspeech.utils as du
import audio.utils as au
import audio.segment as aseg
import config as cfg


deepspeech_model = ds.get_model_object(cfg.model_dir)


DeepSpeechPrediction = namedtuple(
    'DeepSpeechPrediction', ['audio_file', 'transcript', 'confidence']
)


def run_inference(input_audio: str, aggressive: int = 1):

    file_name = os.path.basename(input_audio)
    file_name_base, ext = file_name.split('.')
    # Run VAD on the input file
    segments, sample_rate, audio_length = aseg.vad_segment_generator(input_audio, aggressive)

    results = []

    for i, segment in enumerate(segments):
        # Run deepspeech on the chunk that just completed VAD
        logging.debug("Processing chunk %002d" % (i,))
        output = infer_audio(segment, sample_rate)
        clip_name = "{}_chunk_{}.{}".format(file_name_base, str(i+1), ext)
        clip_path = os.path.join(cfg.clip_output_path, clip_name)
        au.write_wave(clip_path, segment, sample_rate)
        result = DeepSpeechPrediction(clip_name, output.get("sentence", ""), output.get("confidence", ""))
        print(result)
        results.append(result)


def infer_audio(audio_segment: object, sample_rate: int, model_obj: object = deepspeech_model) -> Dict:
    audio = np.frombuffer(audio_segment, dtype=np.int16)
    outputs = ds.stt(model_obj, audio, sample_rate)
    output = du.metadata_json_output(outputs[0])
    return output


if __name__ == "__main__":
    wave_file = sys.argv[1]
    aggressive = sys.argv[2]
    run_inference(wave_file, aggressive)
