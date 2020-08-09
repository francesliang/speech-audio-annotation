FROM python:3.7

#RUN git clone https://github.com/mozilla/DeepSpeech ./models/deepspeech/DeepSpeech/

#RUN cd ./models/deepspeech/DeepSpeech && \
#    pip install --upgrade  wheel==0.34.2 setuptools==46.1.3 && \
#    pip install --upgrade -e .

RUN apt-get update && apt-get install -y sox libsox-fmt-mp3

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
RUN pip install -r models/deepspeech/DeepSpeech/requirements.txt

CMD ["uwsgi", "uwsgi.ini"]
