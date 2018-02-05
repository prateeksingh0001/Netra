"""Netra Vision GCP Library

    Authors:
            Subhojeet Pramanik
            Prateek Singh


"""
import io
import os

import google.cloud.vision


def init_vision():
    vision_client = google.cloud.vision.ImageAnnotatorClient()


def label_captions(img_file):
    with io.open(img_file, 'rb') as image_file:
        content = image_file.read()

    # Use Vision to label the image based on content.
    image = google.cloud.vision.types.Image(content=content)
    response = vision_client.label_detection(image=image)

    print('Labels:')
    for label in response.label_annotations:
        print(label.description)
    return None


