import os
from typing import List

import audio.utils as au
import audio.segment as aseg
import config as cfg


def split_audio_to_files(input_audio: str, aggressive: int = 1) -> List:
    file_name = os.path.basename(input_audio)
    file_name_base, ext = file_name.split('.')
    # Run VAD on the input file
    segments, sample_rate, audio_length = aseg.vad_segment_generator(input_audio, aggressive)

    results = []

    for i, segment in enumerate(segments):
        # Run deepspeech on the chunk that just completed VAD
        clip_name = "{}_chunk_{}.{}".format(file_name_base, str(i+1), ext)
        clip_path = os.path.join(cfg.clip_output_path, clip_name)

        # Write audio data to file
        au.write_wave(clip_path, segment, sample_rate)
        results.append(clip_name)

    return results

