from edge_detector.exceptions import InvalidRGBImage
import numpy as np

class ImageValidator:
    RGB_CHANNELS = 3
    ONE_CHANNEL = 1

    def __init__(self, image) -> None:
        self.image = image
        self.__validate_image()
        self.is_numpy_array()

    def __validate_image(self):
        if not self.is_numpy_array():
            raise InvalidRGBImage
        self.get_number_of_channels()

    def get_number_of_channels(self):
        if self.__has_two_dimensions():
            return self.ONE_CHANNEL
        elif self.__has_three_dimensions():
            return self.image.shape[-1]
        raise InvalidRGBImage

    def __has_two_dimensions(self):
        return self.image.ndim == 2

    def __has_three_dimensions(self):
        return self.image.ndim == 3

    def is_numpy_array(self):
        return isinstance(self.image, np.ndarray)

    def is_rgb(self):
        channels = self.get_number_of_channels()
        return channels == self.RGB_CHANNELS

    def has_one_channel(self):
        channels = self.get_number_of_channels()
        return channels == self.ONE_CHANNEL

    def has_one_or_three_channels(self):
        return self.is_rgb() or self.has_one_channel()
