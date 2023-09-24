import cv2
import cv2.aruco as arm
import numpy as np
import os
from pygame import mixer
import requests
import imutils
import time

count = 0

from tkinter import *
import pygame


def counter():
    global count
    count += 12.5
    print(count)


b = False
mixer.init()
mixer.music.load('1_part.mp3')


def one():
    mixer.music.play()


id_0 = [[0], [1], [2], [3], [4], [5], [6], [7]]

mixer.init()

print("package imported")

ids0 = np.zeros(8, dtype=int)
id_2 = np.zeros(8, dtype=int)


def chnone_1(ids, ids1):
    ids = 0 if ids is None else ids
    ids1 = 0 if ids1 is None else ids1


def chnone(ids, ids1):
    mixer.music.load('1_part.mp3')
    if ids is None:
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


# def find_arm(img, id_1, id_0, id_2, markersize=6, totalmarkers=250, draw=True):
#     global b
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
#     key = getattr(arm, f'DICT_{markersize}X{markersize}_{totalmarkers}')
#     armdict = arm.Dictionary_get(key)
#     armparam = arm.DetectorParameters_create()
#     bboxs, ids, rejected = arm.detectMarkers(thresh1, armdict, parameters=armparam)
#     if draw:
#         arm.drawDetectedMarkers(thresh1, bboxs)
#     chnone(ids)
#     cv2.imshow("threshold image", thresh1)


def find_arm(img, img1, markersize=6, totalmarkers=250, draw=True):
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
    ids0 = ids + ids1
    if draw:
        arm.drawDetectedMarkers(thresh1, bboxs)
    # a = 0
    # if ids & ids1 in ids0:
    #     a = 1
    # if a == 1:
    #     chnone(ids)
    # else:
    #     pass

    cv2.imshow("threshold image", thresh1)
    cv2.imshow("image 2", thresh2)


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Symphony")
        self.root.geometry("1000x700+100+0")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()
        self.shapeframe = LabelFrame(self.root, text="Shapes", font=("times new roman", 15, "bold"), bg="grey",
                                     fg="white", bd=5, relief=GROOVE)
        self.shapeframe.place(x=0, y=0, width=1000, height=500)
        # matrix Labels
        a00 = LabelFrame(self.shapeframe, bd=5)
        a00.place(x=0, y=0, width=333, height=150)
        a01 = LabelFrame(self.shapeframe, bd=5)
        a01.place(x=333, y=0, width=333, height=150)
        a02 = LabelFrame(self.shapeframe, bd=5)
        a02.place(x=666, y=0, width=333, height=150)
        a10 = LabelFrame(self.shapeframe, bd=5)
        a10.place(x=0, y=150, width=333, height=150)
        a11 = LabelFrame(self.shapeframe, bd=5)
        a11.place(x=333, y=150, width=333, height=150)
        a12 = LabelFrame(self.shapeframe, bd=5)
        a12.place(x=666, y=150, width=333, height=150)
        a20 = LabelFrame(self.shapeframe, bd=5)
        a20.place(x=0, y=300, width=333, height=150)
        a21 = LabelFrame(self.shapeframe, bd=5)
        a21.place(x=333, y=300, width=333, height=150)
        a22 = LabelFrame(self.shapeframe, bd=5)
        a22.place(x=666, y=300, width=333, height=150)
        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="Navyblue",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=500, width=600, height=150)
        # Inserting Song Track Label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),
                          bg='orange', fg='gold').grid(row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"), bg='orange',
                            fg='gold').grid(row=0, column=1, padx=10, pady=5)
        # ButtonFrame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=600, width=600, height=150)

        plybtn = Button(buttonframe, text="PLAY", command=self.playsong, width=10, height=1,
                        font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10,
                                                                                             pady=5)
        pausebtn = Button(buttonframe, text="PAUSE", command=self.pause, width=8, height=1,
                          font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10,
                                                                                               pady=5)
        unpbtn = Button(buttonframe, text="UNPAUSE", command=self.unpause, width=10, height=1,
                        font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10,
                                                                                             pady=5)
        stpbtn = Button(buttonframe, text="STOP", command=self.stop, width=10, height=1,
                        font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10,
                                                                                             pady=5)

        # song frame
        songframe = LabelFrame(self.root, text="Playlist", font=("times new roman", 15, "bold"), bg="grey", fg="white",
                               bd=5, relief=GROOVE)
        songframe.place(x=600, y=500, width=400, height=330)
        scrol_y = Scrollbar(songframe, orient=VERTICAL)
        self.playlist = Listbox(songframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        a00.after(1000, self.play(a00))
        a21.after(1000, self.play(a21))

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-PLAYING")
        # cap = cv2.VideoCapture(0)
        # cap1 = cv2.VideoCapture(1)
        # """imgaug=cv2.imread("23.png")"""
        # while True:
        #     success, img = cap.read()
        #     success1, img1 = cap1.read()
        #     find_arm(img, img1, ids0)
        #     cv2.waitKey(1)
        # pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # pygame.mixer.music.play()

    def pause(self):
        self.status.set("-PAUSED")
        pygame.mixer.music.pause()

    def stop(self):
        self.status.set("-STOPPED")
        pygame.mixer.music.stop()

    def unpause(self):
        self.status.set("-PLAYING")
        pygame.mixer.music.unpause()

    def play(self, master):
        l = Label(master, text='1', bg="red", width=333, height=333)
        l.pack()


def main():
    root = Tk()
    MusicPlayer(root)
    root.mainloop()
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(1)
    """imgaug=cv2.imread("23.png")"""
    while True:
        success, img = cap.read()
        success1, img1 = cap1.read()
        # findarm(img, img1, id_1, id_2, id_0)
        find_arm(img, img1)
        # armfound1=findarm(img1)

        # if len(armfound[0])!=0:
        #     for bbox, id in zip(armfound[0], armfound[1]):
        #         print(id)
        #         img=augmentAruco(bbox, id, img, imgaug)
        cv2.imshow("image", img)
        cv2.imshow("image through webcam", img1)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
