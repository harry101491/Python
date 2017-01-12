#%matplotlib inline
#from scipy import misc
#from scipy import ndimage
#import matplotlib.pyplot as plt
#import numpy as np

#img = misc.imread('/Users/harshitpareek/Downloads/img1.jpg', mode='RGB')
#imgArray = np.array(img,dtype='uint8')

#rotate_45 = ndimage.rotate(imgArray, -45)

#new_img = misc.imresize(imgArray, (500,500), interp='bilinear')

#misc.imsave('/Users/harshitpareek/Downloads/img1_rotate1.png',rotate_45)


#reshape = rotate_45.reshape((rotate_45.shape[0],-1))

#plt.axis('off')
#plt.imshow(new_img)
#print("shape of file:",new_img.shape)
#print("type of ndarray:",imgArray.dtype)