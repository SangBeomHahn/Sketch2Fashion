# Commented out IPython magic to ensure Python compatibility.
import os
import warnings
warnings.filterwarnings('ignore')

from keras.models import load_model
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np

from utils.data_generator import get_img_for_model

# 여기 바꾸고
gen_model = load_model('/content/drive/MyDrive/학교 계정/프로그래밍 언어 공부 자료/인공지능/BOAZ 18기/ADV 방학/ADV 방학 세션/GAN 공부 실습/최종/output_b4_pts250/models/00790_gen_model.h5')
img_source = get_img_for_model('/content/images.png') # 여기 원하는 이미지 경로
imgs_source = np.array([img_source]) # array of 1 image
imgs_target_fake = gen_model.predict(imgs_source)
imgs_target_fake = (imgs_target_fake + 1) / 2.0

plt.figure(figsize=(5,5)) 
plt.axis('off')
plt.imshow(imgs_target_fake[0])
