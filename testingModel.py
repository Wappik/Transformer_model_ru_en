import collections
import logging
import os
import pathlib
import re
import string
import sys
import time

import numpy as np
import matplotlib.pyplot as plt

import tensorflow_datasets as tfds
import tensorflow_text as text
import tensorflow as tf

def print_translation(sentence, tokens, ground_truth):
    print(f'{"Input:":15s}: {sentence}')
    print(f'{"Prediction":15s}: {str(tokens.decode("utf-8"))}')
    print(f'{"Ground truth":15s}: {ground_truth}')
    print()

reloaded = tf.saved_model.load('drive/MyDrive/Diplom_data/translator')
print(reloaded("это первая книга, которую я сделал.").numpy())

sentence = "Привет мир!"
ground_truth = "Hello world!"

print_translation(sentence, reloaded(sentence).numpy(), ground_truth)

sentence = "это проблема, которую мы должны решить."
ground_truth = "this is a problem we have to solve."

print_translation(sentence, reloaded(sentence).numpy(), ground_truth)

sentence = "и мои соседи дома услышали об этой идее."
ground_truth = "and my neighboring homes heard about this idea ."

print_translation(sentence, reloaded(sentence).numpy(), ground_truth)

sentence = "поэтому я просто очень быстро поделюсь с вами несколькими историями о некоторых волшебных вещах, которые произошли."
ground_truth = "so i \'ll just share with you some stories very quickly of some magical things that have happened ."

print_translation(sentence, reloaded(sentence).numpy(), ground_truth)

sentence = "это первая книга, которую я когда-либо писал."
ground_truth = "this is the first book i've ever done."

print_translation(sentence, reloaded(sentence).numpy(), ground_truth)

sentence = "Я читал о трицератопсе в энциклопедии."
ground_truth = "I read about triceratops in the encyclopedia."

print_translation(sentence, reloaded(sentence).numpy(), ground_truth)


