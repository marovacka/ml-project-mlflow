import urllib.request
from pathlib import Path
import logging
import numpy as np
import pandas as pd


MNIST_DATASET_URL = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"
MNIST_DATASET_NPZ =  "./data/mnist.npz"
MNIST_DATASET_CSV_FILEPATH = "./data/mnist.csv"
PICTURE_SIZE = 28
LABEL = "label"


def _get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    return logger


logger = _get_logger()


def _prepare_mnist_csv():
    npz_data = np.load(MNIST_DATASET_NPZ)
    x_train = npz_data['x_train']
    y_train = npz_data['y_train']
    x_test = npz_data['x_test']
    y_test = npz_data['y_test']

    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1] * x_train.shape[2])
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1] * x_test.shape[2])

    x = np.concatenate((x_train, x_test))
    y = np.concatenate((y_train, y_test))

    df = pd.DataFrame(x, columns=range(1, PICTURE_SIZE * PICTURE_SIZE + 1))
    df[LABEL] = y
    df.to_csv(MNIST_DATASET_CSV_FILEPATH, index=False)
    npz_data.close()

    file_path = Path(MNIST_DATASET_NPZ)
    if file_path.exists():
        file_path.unlink()


def main():
    file_path = Path(MNIST_DATASET_CSV_FILEPATH)
    if not file_path.exists():
        logger.info(f"Download of \'{MNIST_DATASET_URL}\' has started.")
        urllib.request.urlretrieve(MNIST_DATASET_URL, MNIST_DATASET_NPZ)
        _prepare_mnist_csv()
        logger.info(f"File \'{MNIST_DATASET_CSV_FILEPATH}\' prepared.")
    else:
        logger.info(f"File \'{MNIST_DATASET_CSV_FILEPATH}\' already exists.")


if __name__ == "__main__":
    main()
