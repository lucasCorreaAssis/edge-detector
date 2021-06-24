from unittest import TestCase
import unittest
from edge_detector.edge_detector import EdgeDetector
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

if __name__ == '__main__':
    unittest.main()
