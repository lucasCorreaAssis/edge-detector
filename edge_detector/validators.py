import numpy as np

class ImageValidator:
    RGB_CHANNELS = 3

    def is_numpy_array(self, image):
        return isinstance(image, np.ndarray)

    def is_rgb(self, image):
        return image.ndim == self.RGB_CHANNELS
