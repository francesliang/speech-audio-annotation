import os
import sys
from typing import Dict
import logging
import numpy as np

import models.deepspeech.inference as ds
import models.deepspeech.utils as du
import audio.segment as aseg


def run_inference(model_dir: str, input_audio: str, aggressive: int = 1):
    # Point to a path containing the pre-trained models & resolve ~ if used
    model_path = os.path.expanduser(model_dir)

    # Resolve all the paths of model files
    output_graph, lm, trie = ds.resolve_models(model_path)

    # Load output_graph, alpahbet, lm and trie
    model_retval = ds.load_model(output_graph, lm, trie)


    # Run VAD on the input file
    segments, sample_rate, audio_length = aseg.vad_segment_generator(input_audio, aggressive)

    output = None

    for i, segment in enumerate(segments):
        # Run deepspeech on the chunk that just completed VAD
        logging.debug("Processing chunk %002d" % (i,))
        output = infer_audio(model_retval, segment, sample_rate)
        print(output)


def infer_audio(model_retval: object, audio_segment: object, sample_rate: int) -> Dict:
    audio = np.frombuffer(audio_segment, dtype=np.int16)
    outputs = ds.stt(model_retval[0], audio, sample_rate)
    output = du.metadata_json_output(outputs[0])
    return output


if __name__ == "__main__":
    model_dir = sys.argv[1]
    wave_file = sys.argv[2]
    aggressive = sys.argv[3]
    run_inference(model_dir, wave_file, aggressive)
