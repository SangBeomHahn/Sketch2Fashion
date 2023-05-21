# Sketch2Fashion
손그림 의류 검색 서비스


## Introduction

본 프로젝트는 사람이 손으로 그린 의류 스케치를 실제 의류 이미지로 변환하고 변환된 이미지로 실제 쇼핑몰에서 판매하는 상품을 검색하는 서비스를 제공한다.

## ✨ Demo

### modify
<p align ="center">
  <img src = "https://user-images.githubusercontent.com/90328527/222012872-e316b82f-9974-4d4f-a012-0e8dc9f042ce.gif">
</p>

<p align ="center">
  <img src = "https://user-images.githubusercontent.com/90328527/222012941-c73322ef-4afa-4ec6-8bab-915aa5fa79e7.gif">
</p>

### colorization
<p align ="center">
  <img src = "https://user-images.githubusercontent.com/90328527/222012981-040a0d12-5a36-40b6-8187-d2e9121db740.gif">
</p>

<p align ="center">
  <img src = "https://user-images.githubusercontent.com/90328527/222013017-29ead234-71a9-4839-915c-5d2f8014a416.gif">
</p>


### visual search
<p align ="center">
  <img src = "https://user-images.githubusercontent.com/90328527/222012066-38554844-548d-4cd9-8ae7-bc7c8fbb61c0.gif">
</p>

## Dataset

|Data|데이터 수|Train 데이터 수|Val 데이터 수|세부사항|
|:-:|:-:|:-:|:-:|:-:|
|1|2543|1889|654|hat|
|2|2589|1912|677|pants|
|3|2549|1892|657|t-shirts|
|4|2537|1818|689|651|skirt|


학습에는 fashion-outfit-items 데이터 셋을 활용, 카테고리 별로 약 2500개로 구성된다.

출처 : https://www.kaggle.com/datasets/kritanjalijain/fashionoutfititems

## Model

![project_pipeline](https://github.com/SangBeom-Hahn/Sketch2Fashion/blob/main/assests/model.png)


전체적인 파이프라인은 2 stage로 이루어져 있다. 1단계에서도 2개로 나뉜다. A는 고객이 그린 의류 sketch를 채색 모델을 통해 채색을 하는 것이고 B는 고객이 그린 의류 sketch를 실제 의류 이미지로 변환하는 것이다. A는 sketch에 고객이 원하는 색으로 점을 찍거나 선을 그리는 등 단순한 처리로 완벽한 채색 결과를 생성해 내고 검은색 선으로 스케치의 영역을 구분하는 등 커스터마이징을 할 수 있다. 

2단계에서는 1단계에서 나온 결과물을 MS visual search API의 입력으로 넣어 실제로 입력 이미지와 유사한 제품을 판매하고 있는 쇼핑몰의 URL을 반환한다.

## Project Structure

```
Sketch2Fashion
├── utils
├── root
    ├── model
    ├── static
    ├── templates
    └── views
├── create_training_set.py
├── generate_image.py
└── train_gan.py
```

- utils : 유틸리티 모듈 폴더
- root : 어플리케이션 루트 폴더
    - model : 카테고리별 채색 모델 적재 폴더
    - static : 웹페이지 구성에 필요한 리소스를 모아놓은 폴더
    - templates : 웹페이지 템플릿 폴더
    - views : 라우팅 함수 구현 폴더
- create_training_set.py : 이미지 pair 구성 코드
- generate_image.py : inference 코드
- train_gan.py : train 코드


## Requirements
```
tensorflow==2.x
tensorflow-GPU==2.x
```

## reference
- [Sketch2Fashion: Generating clothing visualization from sketches](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/24693891-8915-4e8b-94b9-5a98831188f0/55752208.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221220T093913Z&X-Amz-Expires=86400&X-Amz-Signature=2822a6743f941bcbc812850571d23c7ac23cd3c2d4f08c3e383aa91a7dd60fe2&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%2255752208.pdf%22&x-id=GetObject)
- [Generative Visual Manipulation on the Natural Image Manifold](https://arxiv.org/abs/1609.03552)
- [Pix2pix-edges-with-color](https://github.com/michaelnation26/pix2pix-edges-with-color)
- [Sketch Your Own GAN](https://arxiv.org/abs/2108.02774)
- [DeepFaceDrawing: Deep Generation of Face Images from Sketches](http://geometrylearning.com/paper/DeepFaceDrawing-supple.pdf)

## Author

👤 **SangBoem-Hahn**

- Github: [@SangBoem-Hahn](https://github.com/SangBeom-Hahn)
- Blog : [Tistory(Sketch2Fashion)](https://hsb422.tistory.com/entry/%EC%86%90%EA%B7%B8%EB%A6%BC-%EC%9D%98%EB%A5%98-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-with-BOAZ)
---
