
import os
import pandas as pd
from typing import List
from collections import namedtuple

from annotations.base import Annotation


DeepSpeechLabel = namedtuple('DeepSpeechLabel', ['id', 'path', 'sentence'])


class DeepSpeechAnnotation(Annotation):

    def __init__(self, fields: List):
        super(DeepSpeechAnnotation, self).__init__(fields)

        self.df = pd.DataFrame(columns=fields)

    def format_output(self, label: DeepSpeechLabel):
        self.df = self.df.append(label._asdict())


    def write_output(self, output_path: str):
        self.df.to_csv(output_path)

