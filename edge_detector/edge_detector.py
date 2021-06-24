from edge_detector.validators import ImageValidator
import cv2
import numpy as np
from edge_detector.exceptions import InvalidRGBImage

class EdgeDetector:
    NUM_CHANNELS = 3

    @classmethod
    def from_image(cls, image):
        return cls(image)

    def __init__(self, image) -> None:
        self.__validate_image(image)
        self.image = image

    def __validate_image(self, image):
        image_validator = ImageValidator()
        if not image_validator.is_numpy_array(image):
            raise InvalidRGBImage
        if not image_validator.is_rgb(image):
            raise InvalidRGBImage

    def detect(self):
        return self.image

