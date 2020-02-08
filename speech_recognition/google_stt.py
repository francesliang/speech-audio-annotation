from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io


def recognise(file_path, lang_code="en-US", sample_rate=16000):
    """
    Transcribe a short audio file using synchronous speech recognition
    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    recognised_results = {}

    client = speech_v1.SpeechClient()

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": lang_code,
        "sample_rate_hertz": sample_rate,
        "encoding": encoding,
    }
    with io.open(file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    results = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        results.append(alternative)

    transcript = '. '.join([r.transcript for r in results])
    recognised_results["transcript"] = transcript

    return recognised_results

