import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# img1 = cv2.imread('/img/woman2.jpg')
# img2 = cv2.imread('/img/woman3.jpg')
# img3 = cv2.imread('/img/woman4.jpg')

notebook_dir = os.getcwd()
 
# 이미지 파일의 상대 경로 설정
img_path = os.path.join(notebook_dir, 'img', 'woman2.jpg')
img1 = cv2.imread(img_path)

# # Convert BGR to RGB
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

plt.subplot(1,3,1)  #1행 3열 중에 1번째
plt.imshow(img1[:,:,(2,1,0)])
plt.xticks([]); plt.yticks([])



# Display the image using Matplotlib
plt.imshow(img1_rgb)
plt.axis('off')  # Optional: Turn off axis labels
plt.show()

# plt.subplot(1,3,1)  #1행 3열 중에 1번째
# plt.imshow(img1[:,:,(2,1,0)])
# plt.xticks([]); plt.yticks([])

# plt.subplot(1,3,2)  #1행 3열 중에 2번째
# plt.imshow(img2[:,:,(2,1,0)])
# plt.xticks([]); plt.yticks([])

# plt.subplot(1,3,3)    #1행 3열 중에 3번째
# plt.imshow(img3[:,:,(2,1,0)])
# plt.xticks([]); plt.yticks([])
# plt.show()