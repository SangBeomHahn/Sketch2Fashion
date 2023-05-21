from flask import Blueprint, render_template, request
import requests
import warnings
warnings.filterwarnings('ignore')

from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from adv.utils.data_generator import get_img_for_model


bp = Blueprint('image', __name__, url_prefix='/image')

@bp.route('/upload_image/', methods=['POST'])
def upload_image_file():
    if request.method == 'POST':
        file = request.files['uploaded_image'] # 이미지 받기
        if not file: return render_template('image.html', label="No Files")
        label = file.filename
        
        
        file.save('ADV/static/'+label) # 그리고 파일을 서버에 저장한다.
        return render_template('image.html', label = label) # 다시 이미지를 출력하기 위해서 파일을 변수로 준다.

@bp.route('/image_colorization', methods=['POST'])
def image_colorization():
        
    label = "ADV/static/down"
    give_label = '/static/down'

    toggle = request.form.get('clothes')

    if toggle == 'pre_toggle_0':
        gen_model = load_model('ADV/model/up/00275_gen_model.h5')

    elif toggle == 'pre_toggle_1':
        gen_model = load_model('ADV/model/down/00310_gen_model.h5')

    elif toggle == 'pre_toggle_2':
        gen_model = load_model('ADV/model/hat/00270_gen_model.h5')

    elif toggle == 'pre_toggle_3':
        gen_model = load_model('ADV/model/skirt/00300_gen_model.h5')
    

    img_source = get_img_for_model(label+".png") # 여기 원하는 이미지 경로
    imgs_source = np.array([img_source]) # array of 1 image
    imgs_target_fake = gen_model.predict(imgs_source)
    imgs_target_fake = (imgs_target_fake + 1) / 2.0
    result_img = imgs_target_fake[0]

    plt.imsave(label+"_changed.png", result_img)

    # 결과 리턴
    return render_template('colorization.html', label=give_label)

@bp.route('/search/')
def search():
    BASE_URI = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
    SUBSCRIPTION_KEY = 'c0bdced4f3cb4de8a7d8fd475e70a817'
    HEADERS = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}
    imagePath = "ADV/static/down_changed.png"
    file = {'image' : ('myfile', open(imagePath, 'rb'))}
    try:
        response = requests.post(BASE_URI, headers=HEADERS, files=file)
        response.raise_for_status()
        res = response.json()
    
    except Exception as ex:
        raise ex

    searchResult = res['tags'][0]['actions'][2]['data']['value']
    webContent = [[i['webSearchUrl'], i['contentUrl'], i['hostPageUrl']] for i in searchResult]

    width = "200"
    height = "200"

    return render_template('search.html', width = width, height = height, pictures=webContent) 