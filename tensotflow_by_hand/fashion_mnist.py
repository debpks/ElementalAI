import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


fashion_df = tf.keras.datasets.fashion_mnist
(fashion_train_images,fashion_train_labels),(fashion_test_images,fashion_test_labels) = fashion_df.load_data()
####### FASHION-MNIST DATASET #######
""" 
0:T-shirt/top
1:Trouser
2:Pullover
3:Dress
4:Coat
5:Sandal
6:Shirt
7:Sneaker
8:Bag
9:Ankle boot
"""
#####################################
####### Explore & Preprocessing Data #######

def preprocess_images(dataset):
    ds_min = np.min(dataset)
    ds_max = np.max(dataset)
    if ds_min == 0 and ds_max == 255:
        dataset = dataset/255.0
    dataset = dataset.reshape(dataset.shape[0],28,28,1)
    dataset = dataset.astype('float32')
    return dataset

fashion_train_images = preprocess_images(fashion_train_images)
fashion_test_images = preprocess_images(fashion_test_images)

plt.imshow(fashion_train_images[0].reshape(28,28))
plt.colorbar()
plt.show()
print(fashion_train_images[0])
np.set_printoptions(linewidth=200)