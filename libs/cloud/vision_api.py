"""Netra Vision GCP Library

    Authors:
            Subhojeet Pramanik
            Prateek Singh
"""


import io
import os
from google.cloud import vision
from google.cloud.vision import types 

def label_captions(img_file):

    vision_client = vision.ImageAnnotatorClient() 

    with io.open(img_file, 'rb') as image_file:
        content = image_file.read()

    # Use Vision to label the image based on content.
    image = vision.types.Image(content=content)
    response = vision_client.label_detection(image=image)

    print('Labels:')
    for label in response.label_annotations:
        print(label.description)
    return None


