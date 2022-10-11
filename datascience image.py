import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
tf.config.experimental.list_physical_devices()
tf.test.is_built_with_cuda()tf.test.is_built_with_cuda()
(X_train, y_train), (X_test,y_test) = tf.keras.datasets.cifar10.load_data()
X_train.shape
Y_train.shape
plot_sample(1)
plot_sample(2)
plot_sample(0)
