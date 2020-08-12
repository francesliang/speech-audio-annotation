FROM python:3.7

#RUN git clone https://github.com/mozilla/DeepSpeech ./models/deepspeech/DeepSpeech/

#RUN cd ./models/deepspeech/DeepSpeech && \
#    pip install --upgrade  wheel==0.34.2 setuptools==46.1.3 && \
#    pip install --upgrade -e .

### Download pretrained model and its checkpoint
#RUN cd ./outputs/ && \ 
#    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz \
#    tar xvfz deepspeech-0.6.1-models.tar.gz \
#    rm deepspeech-0.6.1-models.tar.gz \
#    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-checkpoint.tar.gz \
#    tar xvfz deepspeech-0.6.1-checkpoint.tar.gz 
#    rm deepspeech-0.6.1-checkpoint.tar.gz

RUN apt-get update && apt-get install -y sox libsox-fmt-mp3

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
RUN pip install -r models/deepspeech/DeepSpeech/requirements.txt

CMD ["uwsgi", "uwsgi.ini"]
