import numpy as np
import playsound as playsound

id0 = np.arange(0, 8, dtype=int)
def play(ids, id0):
    for ids in id0:
        if ids == id0:
            continue
        else:
            playsound('/Resources/1.wav')