import os
import subprocess as sp
import asyncio

import config as cfg
from models.utils import split_data


def transform_training_data():
    ### Convert training data
    # "bin/import_cv2.py samples"
    import_cmd = [
        "python3",
        os.path.join(cfg.deepspeech_path, "bin/import_cv2.py"),
        cfg.annotation_output_path
    ]
    import_ps = sp.Popen(import_cmd, stdout=sp.PIPE, stderr=sp.STDOUT)
    outs, errs = import_ps.communicate()
    is_succeed = bool(outs)
    print("Transform training data succeed: {}".format(is_succeed))
    return is_succeed


def run_training(annotation_tsv, epochs=cfg.epochs, lr=cfg.learning_rate):

    ### Split training dataset
    print("Split training data from: {}".format(annotation_tsv))
    split_data(annotation_tsv, cfg.annotation_output_path)

    ### Convert training data
    if not transform_training_data():
        print("Unable to transform training data.Training aborted.")
        return

    ### Run model training
    # "python3 DeepSpeech.py --n_hidden 2048 --checkpoint_dir /Users/xin/Projects/speech-audio-annotation/deepspeech-0.6.1-models --epochs 3 --train_files ../speech-audio-annotation/samples/clips/train.csv --dev_files ../speech-audio-annotation/samples/clips/dev.csv --test_files ../speech-audio-annotation/samples/clips/test.csv --learning_rate 0.0001 --export_dir ../speech-audio-annotation"
    train_cmd = [
        "python3",
        os.path.join(cfg.deepspeech_path, "DeepSpeech.py"),
        "--n_hidden",
        str(cfg.n_hidden),
        "--checkpoint_dir",
        cfg.checkpoint_dir,
        "--epochs",
        str(epochs),
        "--train_files",
        cfg.train_files,
        "--dev_files",
        cfg.dev_files,
        "--test_files",
        cfg.test_files,
        "--learning_rate",
        str(lr),
        "--export_dir",
        cfg.export_dir,
        "--load_cudnn"
    ]
    print("Start model training for {} epochs with learning rate: {}".format(str(epochs), str(lr)))
    sp.Popen(train_cmd)
