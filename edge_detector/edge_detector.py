from edge_detector.validators import ImageValidator
import cv2
import numpy as np
from edge_detector.exceptions import InvalidRGBImage

class EdgeDetector:
    @classmethod
    def from_image(cls, image):
        return cls(image)

    def __init__(self, image) -> None:
        self.__validate_image(image)
        self.image = image

    def __validate_image(self, image):
        image_validator = ImageValidator(image)
        if not image_validator.is_numpy_array():
            raise InvalidRGBImage
        if not image_validator.has_one_or_three_channels():
            raise InvalidRGBImage

    def detect(self):
        edges = cv2.Canny(self.image, 100, 200)
        return edges
