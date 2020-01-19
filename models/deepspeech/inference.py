import os
import glob
import webrtcvad
import logging
from deepspeech import Model
from timeit import default_timer as timer

'''
Load the pre-trained model into the memory
@param models: Output Grapgh Protocol Buffer file
@param lm: Language model file
@param trie: Trie file

@Retval
Returns a list [DeepSpeech Object, Model Load Time, LM Load Time]
'''
def load_model(models, lm, trie):
    BEAM_WIDTH = 500
    LM_ALPHA = 0.75
    LM_BETA = 1.85

    model_load_start = timer()
    ds = Model(models, BEAM_WIDTH)
    model_load_end = timer() - model_load_start
    logging.debug("Loaded model in %0.3fs." % (model_load_end))

    lm_load_start = timer()
    ds.enableDecoderWithLM(lm, trie, LM_ALPHA, LM_BETA)
    lm_load_end = timer() - lm_load_start
    logging.debug('Loaded language model in %0.3fs.' % (lm_load_end))

    return [ds, model_load_end, lm_load_end]

'''
Run Inference on input audio file
@param ds: Deepspeech object
@param audio: Input audio for running inference on
@param fs: Sample rate of the input audio file

@Retval:
Returns a list [Inference, Inference Time, Audio Length]

'''
def stt(ds, audio, fs):
    inference_time = 0.0
    audio_length = len(audio) * (1 / fs)

    # Run Deepspeech
    logging.debug('Running inference...')
    inference_start = timer()
    #output = ds.stt(audio)
    output = ds.sttWithMetadata(audio)
    print('meta output', output)
    inference_end = timer() - inference_start
    inference_time += inference_end
    logging.debug('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length))

    return [output, inference_time]

'''
Resolve directory path for the models and fetch each of them.
@param dirName: Path to the directory containing pre-trained models

@Retval:
Retunns a tuple containing each of the model files (pb, lm and trie)
'''
def resolve_models(dirName):
    pb = glob.glob(dirName + "/*.pb")[0]
    logging.debug("Found Model: %s" % pb)

    lm = glob.glob(dirName + "/lm.binary")[0]
    trie = glob.glob(dirName + "/trie")[0]
    logging.debug("Found Language Model: %s" % lm)
    logging.debug("Found Trie: %s" % trie)

    return pb, lm, trie


def get_model_object(model_dir):
    # Point to a path containing the pre-trained models & resolve ~ if used
    model_path = os.path.expanduser(model_dir)

    # Resolve all the paths of model files
    output_graph, lm, trie = resolve_models(model_path)

    # Load output_graph, alpahbet, lm and trie
    model_retval = load_model(output_graph, lm, trie)

    return model_retval[0]

