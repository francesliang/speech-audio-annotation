import os


# Annotation configs
clip_output_path = os.path.expanduser("/app/outputs/clips")
annotation_output_path = os.path.expanduser("/app/outputs/")
#clip_output_path = os.path.expanduser("outputs/clips")
#annotation_output_path = os.path.expanduser("outputs/")


# Model configs
model_dir = "/app/outputs/deepspeech-0.6.1-models"
#model_dir = "outputs/deepspeech-0.6.1-models"
n_hidden = 2048
checkpoint_dir = model_dir
epochs = 3
train_files = os.path.join(clip_output_path, "train.csv")
dev_files = os.path.join(clip_output_path, "dev.csv")
test_files = os.path.join(clip_output_path, "test.csv")
learning_rate = 0.0001
export_dir = model_dir
deepspeech_path = "/app/models/deepspeech/DeepSpeech"
