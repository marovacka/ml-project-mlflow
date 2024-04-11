from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from mnist_classification.prepare_mnist_dataset_csv import PICTURE_SIZE

INPUT_FEATURES = range(1, PICTURE_SIZE * PICTURE_SIZE + 1)
INPUT_FEATURES = [str(input_feature) for input_feature in INPUT_FEATURES]


class MaxScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._input_features = INPUT_FEATURES
        self._scaling_factor = 255.

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        result = X[self._input_features] / self._scaling_factor
        return result
