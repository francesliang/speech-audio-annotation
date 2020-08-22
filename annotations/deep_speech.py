
import os
import pandas as pd
from typing import List
from collections import namedtuple

from annotations.base import Annotation


DeepSpeechLabel = namedtuple('DeepSpeechLabel', ['id', 'path', 'sentence'])


class DeepSpeechAnnotation(Annotation):

    def __init__(self, annotation_file=None):
        super(DeepSpeechAnnotation, self).__init__()

        self.fields = DeepSpeechLabel._fields
        if annotation_file is None or not os.path.exists(annotation_file):
            self.df = pd.DataFrame(columns=self.fields)
        else:
            self.df = pd.read_csv(annotation_file, sep='\t'))

    def format_output(self, label: DeepSpeechLabel):
        self.df = self.df.append(label._asdict(), ignore_index=True)


    def write_output(self, output_path: str):
        self.df.to_csv(output_path, columns=self.fields, sep='\t')

