# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:25:28 2020

@author: MANTHAN WATTAMWAR
"""

import cv2
import numpy as np
url="http://26.56.183.63:8080"
cap=cv2.VideoCapture(url)
while(True):
    ret,frame=cap.read()
    if frame is not None:
        cv2.imshow('Frame',frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()