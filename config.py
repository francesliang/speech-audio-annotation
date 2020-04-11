import os


# Annotation configs
outputs_dir = "/app/outputs/"
# outputs_dir = "outputs/"
clip_output_path = os.path.join(outputs_dir, "clips")
annotation_output_path = outputs_dir

# Model configs
model_dir = os.path.join(outputs_dir, "deepspeech-0.6.1-models")
n_hidden = 2048
checkpoint_dir = model_dir
epochs = 3
train_files = os.path.join(clip_output_path, "train.csv")
dev_files = os.path.join(clip_output_path, "dev.csv")
test_files = os.path.join(clip_output_path, "test.csv")
learning_rate = 0.0001
export_dir = os.path.join(outputs_dir, "trained_models")
deepspeech_path = "/app/models/deepspeech/DeepSpeech"
