import os
import subprocess as sp
import asyncio

import config as cfg


def run_training():
    "python3 DeepSpeech.py --n_hidden 2048 --checkpoint_dir /Users/xin/Projects/speech-audio-annotation/deepspeech-0.6.1-models --epochs 3 --train_files ../speech-audio-annotation/samples/clips/train.csv --dev_files ../speech-audio-annotation/samples/clips/dev.csv --test_files ../speech-audio-annotation/samples/clips/test.csv --learning_rate 0.0001 --export_dir ../speech-audio-annotation"
    cmd = [
        "python3",
        os.path.join(cfg.deepspeech_path, "DeepSpeech.py"),
        "--n_hidden",
        str(cfg.n_hidden),
        "--checkpoint_dir",
        cfg.checkpoint_dir,
        "--epochs",
        str(cfg.epochs),
        "--train_files",
        cfg.train_files,
        "--dev_files",
        cfg.dev_files,
        "--test_files",
        cfg.test_files,
        "--learning_rate",
        str(cfg.learning_rate),
        "--export_dir",
        cfg.export_dir
    ]
    print("start run_training")
    sp.Popen(cmd)
