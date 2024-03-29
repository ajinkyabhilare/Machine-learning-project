# -*- coding: utf-8 -*-
"""Image recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LT3WSzWF_nhlRrhXau4bZSxpdYvfnkik
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

bg=cv2.imread("PID.JPG")
bg=cv2.cvtColor(bg,cv2.COLOR_BGR2RGB)

plt.imshow(bg)

bg.shape

valve=cv2.imread("symbol1.JPG")

plt.imshow(valve)

valve.shape
height,width,channels=valve.shape

methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for x in methods:
  bg_copy=bg.copy()
  method=eval(x)
  result=cv2.matchTemplate(bg_copy,valve,method)
  plt.imshow(result)

for x in methods:
  bg_copy=bg.copy()
  method=eval(x)
  result=cv2.matchTemplate(bg_copy,valve,method)
  min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
  if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
    top_left=min_loc
  else:
    top_left=max_loc
    bottom_right=(top_left[0] + width,top_left[1] + height)
    cv2.rectangle(bg_copy,top_left,bottom_right,255,10)

    plt.subplot(121)
    plt.imshow(result)
    plt.title("Result of template matching")

    plt.subplot(122)
    plt.imshow(bg_copy)
    plt.title("Match Point")


    plt.show()

import csv
f=open('Inst.csv','w+',newline='')
lnwriter= csv.writer(f)
lnwriter.writerow(['control_valve'])
f.close()



"""# New Section

# New Section

# New Section
"""