"""
Recognize food: fruit, vegetable
"""

import io
import os
import voice
from datetime import datetime

import cv2
from google.cloud import vision_v1p3beta1 as vision

# Setup google authen client key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

# Source path content all images
SOURCE_PATH = "C:/Users/maie4/food-recognition/img"

FOOD_TYPE = 'Fruit'  # 'Vegetable'


def load_food_name(food_type):
    """
    Load all known food type name.
    :param food_type: Fruit or Vegetable
    :return:
    """
    names = [line.rstrip('\n').lower() for line in open('dict/' + food_type + '.dict')]
    return names


def recognize_food(img_path, list_foods):
    start_time = datetime.now()

    # opencv로 이미지 읽기
    img = cv2.imread(img_path)

    # 이미지 크기 가져오기
    height, width = img.shape[:2]

    # 이미지 축적
    img = cv2.resize(img, (800, int((height * 800) / width)))

    # 임시 파일에 이미지 저장
    cv2.imwrite(SOURCE_PATH + "output.jpg", img)

    # google vision에 대한 새로운 img 경로 만들기
    img_path = SOURCE_PATH + "output.jpg"

    # Google 비전 클라이언트 만들기
    client = vision.ImageAnnotatorClient()

    # 이미지 파일 읽기
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        desc = label.description.lower()
        score = round(label.score, 2)
        print("label: ", desc, "  score: ", score) #과일이름 정확도
        if (desc in list_foods):

	    voice.speech("%s가 있습니다." % desc.upper()) #정확도 높은 순으로 과일이름 출력
            # Get first fruit only
            break


print('---------- Start FOOD Recognition --------')
list_foods = load_food_name(FOOD_TYPE)
print(list_foods)
path = SOURCE_PATH + '1.jpg'
recognize_food(path, list_foods)
print('---------- End ----------')
