import cv2
import cv2.aruco as arm
import time
from pygame import mixer

count = 0

ids_0 = [[0], [1], [2], [3], [4], [5], [6], [7]]

b = True


def counter():
    global count
    count += 12.5
    print(count)


def one():
    mixer.music.play()


def not_none_0(ids):
    ids = None or 0
    return ids


def not_none(ids, ids1):
    ids = None or 0
    ids1 = None or 0
    return ids + ids1


def check_all(ids, ids1, ids_0):
    global b
    not_none(ids, ids1)
    if (ids + ids1) == ids_0:
        b = True
    else:
        pass
    return b


def check_all_0(ids, ids_0):
    global b
    not_none_0(ids)
    if ids == ids_0:
        b = True
    return b


def chnone(ids):
    # mixer.music.load('1_part.mp3')
    # if ids is None and ids1 is None:
    #     pass
    if b:
        pass
    elif ids[0] != [0]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('2_part.mp3')
    elif ids[1] != [1]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('3_part.mp3')
    elif ids[2] != [2]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('4_part.mp3')
    elif ids[3] != [3]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('5_part.mp3')
    elif ids[4] != [4]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('6_part.mp3')
    elif ids[5] != [5]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('7_part.mp3')
    elif ids[6] != [6]:
        one()
        time.sleep(10)
        counter()
        mixer.music.load('8_part.mp3')
    elif ids[7] != [7]:
        one()
        time.sleep(10)
        counter()
    print(ids)


def find_arm(img, ids_0, markersize=6, totalmarkers=250, draw=True):
    # global b
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)[1]
    #     thresh2 = cv2.threshold(gray2, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #     imgray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(arm, f'DICT_{markersize}X{markersize}_{totalmarkers}')
    armdict = arm.Dictionary_get(key)
    armparam = arm.DetectorParameters_create()
    # bboxs, ids, rejected = arm.detectMarkers(thresh1, armdict, parameters=armparam)
    bboxs, ids, rejected = arm.detectMarkers(thresh1, armdict, parameters=armparam)
    if ids is None:
        ids = 0
    #     bboxs1, ids1, rejected1 = arm.detectMarkers(thresh2, armdict, parameters=armparam)
    #     chnone(ids, ids1)
    # print(ids)
    if draw:
        arm.drawDetectedMarkers(thresh1, bboxs)
    # b = (ids == id_0)
    # while b:
    cv2.imshow("threshold image", thresh1)
    # check_all_0(ids, ids_0)
    chnone(ids)


def main():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        find_arm(img, ids_0)


if __name__ == "__main__":
    main()
