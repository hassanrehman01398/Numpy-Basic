# -*- coding: utf-8 -*-
"""
sCreated on Wed Oct  9 11:11:35 2019

@author: Muhammad Hassan Ur Rehman
"""
'''
import numpy as np
import matplotlib.pyplot as plt
im=plt.imread("C:\\Users\\hp\\Desktop\\images\\1.jpg")
print(type(im))
print(im.shape)
print()
'''
#%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image as im
'''
for i in range(21):
    img=mpimg.imread('C:\\Users\\hp\\Desktop\\images\\'+str(i+1)+'.jpg')
    imgplot = plt.imshow(img)
    plt.show()
'''
list1=[]
for i in range(20):
    im1=(im.open('C:\\Users\\hp\\Desktop\\images\\'+str(i+1)+'.jpg'))
    im1=im1.resize((500,500),im.ANTIALIAS)
 #   print(plt.imshow(im1))
    im1.save('resize'+str(i+1)+'.jpg')
    list1.append(np.array(im1))
#    print(a1)
print(list1[19])