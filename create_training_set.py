import warnings
warnings.filterwarnings('ignore')
import glob
import os

import cv2
from keras_preprocessing.image import load_img, save_img
from keras.utils import get_file
import numpy as np

from utils import config

# mkdir data/validation/target
# mkdir data/validation/source

# Define Functions
def create_source_imgs(target_dir, source_dir):
    pathname = f'{target_dir}/*.jpg' 
    for filepath in glob.glob(pathname):
        img_target = load_img(filepath, target_size=(config.IMG_HEIGHT, config.IMG_WIDTH))
        img_target = np.array(img_target)
        img_source = detect_edges(img_target) 
        filename = os.path.basename(filepath)
        img_source_filepath = os.path.join(source_dir, filename)
        save_img(img_source_filepath, img_source) 


# 나는 모자니깐 hat/*.jpg이고 hat은 폴더 명으로 hat이라는 폴더에 jpg들이 다 들어있는 것
def create_target_images():
    pathname = 'hat/*.jpg' # 여기 경로를 변경
    for filepath in glob.glob(pathname):
        filename = os.path.basename(filepath)
        img_target = load_img(filepath, target_size=(config.IMG_HEIGHT, config.IMG_WIDTH))
        img_target = np.array(img_target)
        img_target_filepath = os.path.join(config.TRAINING_TARGET_DIR, filename) 
        save_img(img_target_filepath, img_target) 

def detect_edges(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_gray = cv2.bilateralFilter(img_gray, 5, 50, 50)
    img_gray_edges = cv2.Canny(img_gray, 45, 100)
    img_gray_edges = cv2.bitwise_not(img_gray_edges) 
    img_edges = cv2.cvtColor(img_gray_edges, cv2.COLOR_GRAY2RGB)
    
    return img_edges

def resize_imgs_in_directory(img_dir):
    for filepath in glob.glob(f'{img_dir}/*.jpg'):
        img = load_img(filepath, target_size=(config.IMG_HEIGHT, config.IMG_WIDTH))
        img = np.array(img)
        save_img(filepath, img)

#  Training Set

# 이거를 돌리면 data/training/target 폴더에 원본 데이터가 생김
create_target_images()
# 이걸 돌리면 data/training/source 폴더에 엣지 데이터가 생김
create_source_imgs(config.TRAINING_TARGET_DIR, config.TRAINING_SOURCE_DIR) # hat을 다른 걸로 바꾸기

# 'data/validation'/target
resize_imgs_in_directory(config.VALIDATION_TARGET_DIR)
create_source_imgs(config.VALIDATION_TARGET_DIR, config.VALIDATION_SOURCE_DIR)
