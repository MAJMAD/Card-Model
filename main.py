import cv2 as cv
import numpy as np
import os
from time import time
from PIL import ImageGrab
from Vision import Vision
#from windowcapture import WindowCapture

wincap = ImageGrab.grab()
wincap_np = np.array(wincap)
wincap_rgb = cv.cvtColor(wincap_np, cv.COLOR_BGR2RGB)
cap = cv.VideoCapture(0)
loop_time = time()

cascade_card = cv.CascadeClassifier('cascade/cascade.xml')
vision_card = Vision(None)

while(True):

    ret, screenshot = cap.read()


    rectangles = cascade_card.detectMultiScale(screenshot)

    detection_image = vision_card.draw_rectangles(screenshot, rectangles)

    cv.imshow('Unprocessed', screenshot)
    loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        #wincap = ImageGrab.grab()
        #wincap_np = np.array(wincap)
        #creenshot = cv.cvtColor(wincap_np, cv.COLOR_BGR2RGB)
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        #wincap = ImageGrab.grab()
        #wincap_np = np.array(wincap)
        #screenshot = cv.cvtColor(wincap_np, cv.COLOR_BGR2RGB)
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)


