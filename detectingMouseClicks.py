import cv2
import numpy as np
import pyttsx3

circles = np.zeros((4,2),np.int)
cnt = 0

def mouseClick(event,x,y,flags,perimeter):
    global cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        circles[cnt] = x,y
        cnt += 1
        print(circles)

img = cv2.imread('coffee.jpg')
img = cv2.resize(img,(1400,900))
speak = pyttsx3.init()
spk = 0
while True:
    if cnt == 4:
        width, height = 700,850#250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        # print(pts1)
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow('Output Image', imgOutput)
        if spk == 0:
            speak.say('successful')  # text are ready to speak
            speak.runAndWait()  # starting speaking
            spk=1

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 10, (0, 0, 255), cv2.FILLED)

    cv2.imshow('book',img)
    cv2.setMouseCallback('book',mouseClick)
    cv2.waitKey(1)