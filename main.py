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
import eel

reloaded = tf.saved_model.load('drive/MyDrive/Diplom_data/translator')

@eel.expose
def get_word(word):
    return str(reloaded(word).numpy().decode("utf-8"))

if __name__ == '__main__':
    print(str(reloaded("Привет").numpy().decode("utf-8")))
    eel.init("web")
    eel.start("index.html", mode="chrome", size=(1190, 430))
