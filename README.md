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

## Features
1. 스케치 업로드
2. sketch를 실사로 변환
3. 유사 이미지 검색
    - 유사한 제품을 판매하는 쇼핑몰로 연결



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
- Blog : [Tistory(Sketch2Fashion)](https://hsb422.tistory.com/entry/%EC%86%90%EA%B7%B8%EB%A6%BC-%EC%9D%98%EB%A5%98-%EA%B2%80%EC%83%89-%EC%84%9C%EB%B9%84%EC%8A%A4)
---
