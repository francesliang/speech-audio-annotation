import os
import shutil


def ensure_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def ensure_model_dir(src_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
        for f in os.listdir(src_path):
            shutil.copy(os.path.join(src_path, f), dest_path)
    return dest_path


# Annotation configs
outputs_dir = "/app/outputs/"
outputs_data_dir = os.path.join(outputs_dir, "data")
# outputs_dir = "outputs/"
clip_output_path = ensure_dir(os.path.join(outputs_data_dir, "clips"))
annotation_output_path = outputs_data_dir

# Model configs
orig_model_dir = os.path.join(outputs_dir, "deepspeech-0.6.1-models")
checkpoint_dir = os.path.join(outputs_dir, "deepspeech-0.6.1-checkpoint")
train_files = os.path.join(clip_output_path, "train.csv")
dev_files = os.path.join(clip_output_path, "dev.csv")
test_files = os.path.join(clip_output_path, "test.csv")
export_dir = ensure_model_dir(orig_model_dir, os.path.join(outputs_data_dir, "trained_models"))
model_dir = export_dir
deepspeech_path = "/app/models/deepspeech/DeepSpeech"
n_hidden = 2048
epochs = 3
learning_rate = 0.0001
