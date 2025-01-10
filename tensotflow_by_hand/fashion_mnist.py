import tensorflow as tf
import matplotlib.pyplot as plt

fashion_df = tf.keras.datasets.fashion_mnist
(fashion_train_images,fashion_train_labels),(fashion_test_images,fashion_test_labels) = fashion_df.load_data()

