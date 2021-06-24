from unittest import TestCase
import unittest
from edge_detector.edge_detector import EdgeDetector
from edge_detector.exceptions import InvalidRGBImage
from edge_detector.validators import ImageValidator
import numpy as np

class EdgeDetectorTest(TestCase):
    HEIGHT = 416
    WIDTH = 416
    NUM_CHANNELS = 3

    def setUp(self) -> None:
        return super().setUp()

    def test_to_pass_a_image_as_input(self):
        blank_image = self.__create_blank_image()
        EdgeDetector.from_image(blank_image)

    def __create_blank_image(self):
        return np.zeros((self.HEIGHT, self.WIDTH, self.NUM_CHANNELS), np.uint8)

    def test_from_image_should_raise_on_invalid_image(self):
        with self.assertRaises(InvalidRGBImage):
            EdgeDetector.from_image(0)

    def test_detect_should_return_an_image(self):
        blank_image = self.__create_blank_image()
        edge_detecotr = EdgeDetector.from_image(blank_image)
        output_image = edge_detecotr.detect()
        self.__is_image(output_image)

    def __is_image(self, image):
        image_validator = ImageValidator()
        self.assertTrue(image_validator.is_numpy_array(image))
        self.assertTrue(image_validator.is_rgb(image))

if __name__ == '__main__':
    unittest.main()
