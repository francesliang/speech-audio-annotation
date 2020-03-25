Speech Audio Annotation System [WIP]
--------------------

This tool uses Mozilla [DeepSpeech](https://github.com/mozilla/DeepSpeech) as an example to demonstrate the some generic functionalities / components of a speech-audio annotation tool, including annotation and model inference - training loop, to semi-automate the annotation process.

This repo contains the back-end component of the annotation system, the front-end component [`speech-audio-annotation-ui`](https://github.com/francesliang/speech-audio-annotation-ui) is also required for the usage of the tool.


### Setup Back-end Component

1. Clone the project git repo

2. Download and unzip the pre-trained DeepSpeech model to `<project_root_dir>/outputs`:

```
cd <project_root_dir>/outputs
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz
tar xvf deepspeech-0.6.1-models.tar.gz
```

3. Clone the DeepSpeech repo to `<project_root_dir>/models/deepspeech` (only required if model-training is needed):

```
git clone https://github.com/mozilla/DeepSpeech.git <project_root_dir>/models/deepspeech`
```

4. Build and run `docker-compose` in `<project_root_dir>` to bring up the containers:

```
docker-compose up --build
```

### Setup Front-end Component

1. Clone the UI project repo outside the back-end project repo:

```
git clone https://github.com/francesliang/speech-audio-annotation-ui
```

2. Build and run `docker-compose` in `<project_root_dir>` to bring up the containers:

```
docker-compose up --build
```

3. The URL of the UI should be `localhost:3000` 


### How it works


