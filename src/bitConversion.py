import bitstring
from bitstring import BitArray

import torchaudio
import torch

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv
import io

# b = BitArray(bytes=open('src/test.mp3', 'rb').read())
# print(b.bin)

waveform, sample_rate = torchaudio.load('src/test.mp3')

model = hub.load('https://www.kaggle.com/models/google/yamnet/TensorFlow2/yamnet/1')

scores, embeddings, log_mel_spectrogram = model(waveform)
scores.shape.assert_is_compatible_with([None, 521])
embeddings.shape.assert_is_compatible_with([None, 1024])
log_mel_spectrogram.shape.assert_is_compatible_with([None, 64])

# Find the name of the class with the top score when mean-aggregated across frames.
def class_names_from_csv(class_map_csv_text):
    """Returns list of class names corresponding to score vector."""
    class_names = []
    with tf.io.gfile.GFile(class_map_csv_text) as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader:
        class_names.append(row['display_name'])   
    return class_names


class_map_path = "C:/Users/avamc/Downloads/yamnet-tensorflow2-yamnet-v1/assets/yamnet_class_map.csv"
class_names = class_names_from_csv(tf.io.read_file(class_map_path).numpy().decode('utf-8'))
print(class_names[scores.numpy().mean(axis=0).argmax()])  # Should print 'Silence'.