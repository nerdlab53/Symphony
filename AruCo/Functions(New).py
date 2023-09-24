import cv2 as cv
import numpy as np
from pygame import mixer


def detected(ids, ids1):
    b = False
    if len(ids + ids1) == 8:
        b = True
    while (b):
        pass
    if not b:
        if ([0] not in ids) or ([0] not in ids1):
            mixer.music.play()
            mixer.music.load(' ')
        ...
