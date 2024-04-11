import matplotlib.pyplot as plt
import numpy as np

# from prepare_mnist_dataset_csv import PICTURE_SIZE

def reshape_flatten_images(flatten_images):
    shape = flatten_images.shape
    if len(shape) == 1:
        flatten_images = np.expand_dims(flatten_images, axis=0)
    
    size = int(np.sqrt(flatten_images.shape[1]))

    original_images = flatten_images.reshape(flatten_images.shape[0],
                                             size,
                                             size)
    
    return original_images



