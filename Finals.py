import cv2
import numpy as np
import time
import math

img = cv2.imread('Picture1',cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_yellow = np.array([30,100,50])
upper_yellow = np.array([60,255,255])

lower_red1 = np.array([0, 100, 50])
upper_red1 = np.array([30, 255, 255])
lower_red2 = np.array([150, 100, 50])
upper_red2 = np.array([180, 255, 255])

lower_green = np.array([60,100,50])
upper_green = np.array([90,255,255])

lower_cyan = np.array([90,100,50])
upper_cyan = np.array([120,255,255])

lower_blue = np.array([120,100,50])
upper_blue = np.array([150,255,255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_red = mask1 + mask2
mask_green = cv2.inRange(hsv,lower_green,upper_green)
mask_cyan = cv2.inRange(hsv,lower_cyan,upper_cyan)
mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
mask_yellow = cv2.inRange(hsv,lower_yellow,upper_yellow)
kernel = np.ones((5,5),np.uint8)
erosion_yellow = cv2.erode(mask_yellow,kernel,iterations=1)
dilated_yellow = cv2.dilate(erosion_yellow,kernel,iterations=1)
erosion_red = cv2.erode(mask_red,kernel,iterations=1)
dilated_red = cv2.dilate(erosion_red,kernel,iterations=1)
erosion_green = cv2.erode(mask_green,kernel,iterations=1)
dilated_green = cv2.dilate(erosion_green,kernel,iterations=1)
erosion_blue = cv2.erode(mask_blue,kernel,iterations=1)
dilated_blue = cv2.dilate(erosion_blue,kernel,iterations=1)
erosion_cyan = cv2.erode(mask_cyan,kernel,iterations=1)
dilated_cyan = cv2.dilate(erosion_cyan,kernel,iterations=1)


contours_yellow, hierarchy_y = cv2.findContours(dilated_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours_red, hierarchy_r = cv2.findContours(dilated_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours_green, hierarchy_g = cv2.findContours(dilated_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours_blue, hierarchy_b = cv2.findContours(dilated_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours_cyan, hierarchy_c = cv2.findContours(dilated_cyan,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours_yellow:
    epsilon = 0.1 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    if len(approx)==3:
        #Assign Triangle
    elif len(approx)==4:
        #Assign Square
    else:
        #Assign Circle


for cnt in contours_red:
    epsilon = 0.1 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    if len(approx) == 3:
        # Assign Triangle
    elif len(approx) == 4:
        # Assign Square
    else:
        # Assign Circle



cv2.waitKey(0)
cv2.destroyAllWindows()