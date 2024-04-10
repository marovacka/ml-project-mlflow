import tensorflow as tf
from sklearn.base import BaseEstimator
from mnist_classification.scalers import INPUT_FEATURES
from mnist_classification.prepare_mnist_dataset_csv import PICTURE_SIZE


def categorical_crossentropy_loss(y_true, y_pred):
    # print(y_true.shape)
    # print(y_pred.shape)
    y_true = tf.keras.utils.to_categorical(y_true)    
    y_pred = tf.keras.utils.to_categorical(y_pred)

    loss = tf.keras.losses.categorical_crossentropy(y_true, y_pred)

    return loss



def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax'),
        # tf.keras.layers.Lambda(lambda x: tf.argmax(x, axis=1))
    ])

    model.compile(optimizer='adam',
                #   loss=categorical_crossentropy_loss,
                  loss='categorical_crossentropy',
                  run_eagerly=True,
                  metrics=['accuracy'])

    return model


class Mnist_Cnn_Classifier(BaseEstimator):
    def __init__(self):
        # Define any parameters you need here
        self._model = create_model()
        self._history = None

    def fit(self, X, y):
        # Your training logic goes here
        # For simplicity, let's assume no training is needed for this example

        label = tf.keras.utils.to_categorical(y)
        # label = y.astype('float32')
        input_features = X[INPUT_FEATURES].values
        input_features = input_features.reshape((input_features.shape[0], PICTURE_SIZE, PICTURE_SIZE)).astype('float32')
        self._history = self._model.fit(input_features, label, epochs=5, batch_size=64)

        return self

    def predict(self, X):
        # Your prediction logic goes here
        # For simplicity, let's assume it predicts class 0 for all instances
        input_features = X[INPUT_FEATURES].values
        input_features = input_features.reshape((input_features.shape[0], PICTURE_SIZE, PICTURE_SIZE)).astype('float32')
        return self._model.predict(input_features)
