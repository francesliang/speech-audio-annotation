import os


def ensure_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


# Annotation configs
outputs_dir = "/app/outputs/"
outputs_data_dir = os.path.join(outputs_dir, "data")
# outputs_dir = "outputs/"
clip_output_path = ensure_dir(os.path.join(outputs_data_dir, "clips"))
annotation_output_path = outputs_data_dir

# Model configs
model_dir = os.path.join(outputs_dir, "deepspeech-0.6.1-models")
checkpoint_dir = os.path.join(outputs_dir, "deepspeech-0.6.1-checkpoint")
n_hidden = 2048
epochs = 3
train_files = os.path.join(clip_output_path, "train.csv")
dev_files = os.path.join(clip_output_path, "dev.csv")
test_files = os.path.join(clip_output_path, "test.csv")
learning_rate = 0.0001
export_dir = ensure_dir(os.path.join(outputs_data_dir, "trained_models"))
deepspeech_path = "/app/models/deepspeech/DeepSpeech"
