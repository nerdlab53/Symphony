import cv2
import cv2.aruco as arm
import numpy as np
from pygame import mixer
import time
import threading

count = 0


# Defining the functions and then threading them

class nailing_them_melodies():
    def __init__(self):
        # threading.Thread.__init__(self)
        self.chnone = threading.Thread(target=chnone, args=(ids, ids1))
        self.chnone.daemon = True
        self.chnone.start()
        self.find_arm = threading.Thread(target=find_arm, args=(img, img1))
        self.find_arm.daemon = True
        self.find_arm.start()


def counter():
    global count
    count += 12.5
    print(count)


b = False

mixer.init()


def one():
    mixer.music.play()
    # mixer.music.load('2_part.mp3')


id_0 = [[0], [1], [2], [3], [4], [5], [6], [7]]

mixer.init()

print("package imported")

id_0 = [[0], [1], [2], [3], [4], [5], [6], [7]]

idsT = 0
mixer.init()

print("package imported")

ids0 = np.zeros(8, dtype=int)
id_2 = np.zeros(8, dtype=int)


def chnone_1(ids, ids1, idsT):
    ids = 0 if ids is None else ids
    ids1 = 0 if ids1 is None else ids1
    idsT = ids + ids1
    return idsT


def chnone(ids, ids1):
    mixer.music.load('music/1_part.mp3')
    if ids is None or ids1 is None:
        ids = 0 if ids is None else ids
        ids1 = 0 if ids1 is None else ids1
    elif ids[0] != [0] or ids1[0] != [0]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/2_part.mp3')
    elif ids[1] != [1] or ids1[1] != [1]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/3_part.mp3')
    elif ids[2] != [2] or ids1[2] != [2]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/4_part.mp3')
    elif ids[3] != [3] or ids1[3] != [3]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/5_part.mp3')
    elif ids[4] != [4] or ids1[4] != [4]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/6_part.mp3')
    elif ids[5] != [5] or ids1[5] != [5]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/7_part.mp3')
    elif ids[6] != [6] or ids1[6] != [6]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('music/8_part.mp3')
    elif ids[7] != [7] or ids1[7] != [7]:
        one()
        time.sleep(10)
        counter()
    print(ids)
    print(ids1)


def find_arm(img, img1, markersize = 6, totalmarkers=250, draw=True):
    # global b
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)[1]
    thresh2 = cv2.threshold(gray2, 100, 255, cv2.THRESH_OTSU)[1]
    #     imgray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(arm, f'DICT_{markersize}X{markersize}_{totalmarkers}')
    armdict = arm.Dictionary_get(key)
    armparam = arm.DetectorParameters_create()
    # bboxs, ids, rejected = arm.detectMarkers(thresh1, armdict, parameters=armparam)
    bboxs, ids, rejected = arm.detectMarkers(thresh1, armdict, parameters=armparam)
    bboxs1, ids1, rejected1 = arm.detectMarkers(thresh2, armdict, parameters=armparam)
    chnone(ids, ids1)
    if draw:
        arm.drawDetectedMarkers(thresh1, bboxs)
    cv2.imshow("threshold image", thresh1)
    cv2.imshow("image 2", thresh2)


def main():
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        success1, img1 = cap1.read()
        find_arm(img, img1, idsT)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
