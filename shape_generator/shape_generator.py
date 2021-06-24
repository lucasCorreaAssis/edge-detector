from shape_generator.point import Point
import numpy as np
import cv2 as cv

class ShapeGenerator:
    ONE_CHANNEL = 1
    RGB_CHANNELS = 3
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def get_one_channel_blank_image(self):
        return np.zeros((self.height, self.width, self.ONE_CHANNEL), np.uint8)

    def get_rgb_blank_image(self):
        return np.zeros((self.height, self.width, self.RGB_CHANNELS), np.uint8)

    def draw_square_at_the_center(self, side_size):
        blank_image = self.get_one_channel_blank_image()
        coordinates = self.__get_square_coordinates_based_on_the_image(side_size)
        image = cv.rectangle(
            blank_image,
            coordinates['top_left'].get_point_as_tuple(),
            coordinates['bottom_right'].get_point_as_tuple(),
            (255, 255, 255)
        )
        return image

    def __get_square_coordinates_based_on_the_image(self, side_size):
        center = self.__get_center_of_image()
        coordinates = {}
        coordinates['top_left'] = Point(center.x - side_size, center.y + side_size)
        coordinates['bottom_right'] = Point(center.x + side_size, center.y - side_size)
        return coordinates

    def __get_center_of_image(self):
        half_height = self.height // 2
        half_width = self.height // 2
        return Point(half_width, half_height)
