'''

Inception-V3 using Keras

Notes:
1. Currently WIP and is incomplete. Using architecture based on [2] with features based on [1].
2. Is missing localized response normalization used by [2]. Information about LRN can be found in [3]. However, the
effectiveness of LRN is disputed, and in case studies of convolution networks such as VGGNet, LRN was omitted from the
network [4].
3. Keras implementation of Inception-v3 is trained on ImageNet, automatically making this implementation transfer
learning.

Papers:     [1] https://arxiv.org/pdf/1512.00567v1.pdf
            [2] https://bmcevolbiol.biomedcentral.com/articles/10.1186/s12862-017-1014-z
            [3] http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf
            [4] https://arxiv.org/pdf/1409.1556.pdf

~Dakila Ledesma

'''

from keras.applications.inception_v3 import InceptionV3
from keras.layers import Input, Conv2D, MaxPooling2D, BatchNormalization, AveragePooling2D, Dense
from keras.models import Model, load_model

input_img = Input(shape=(224, 224, 3))  # adapt this if using `channels_first` image data format

x = Conv2D(64, kernel_size=(7, 7), strides=2, activation='relu', padding='same')(input_img)
x = MaxPooling2D(pool_size=(3, 3), strides=2, padding='same')(x)
x = BatchNormalization()(x)
# Missing LRN
x = Conv2D(192, kernel_size=(3, 3), strides=1, activation='relu', padding='same')(x)
x = MaxPooling2D(pool_size=(3, 3), strides=2, padding='same')(x)
x = BatchNormalization()(x)
# Missing LRN
x = InceptionV3()(x)
x = InceptionV3()(x)
x = MaxPooling2D(pool_size=(3, 3), strides=2, padding='same')(x)
x = BatchNormalization()(x)
x = InceptionV3()(x)
x = InceptionV3()(x)
x = InceptionV3()(x)
x = InceptionV3()(x)
x = InceptionV3()(x)
x = MaxPooling2D(pool_size=(3, 3), strides=2, padding='same')(x)
x = BatchNormalization(2, padding='same')(x)
x = InceptionV3()(x)
x = InceptionV3()(x)
x = AveragePooling2D(2, padding='same')(x)
x = BatchNormalization(2, padding='same')(x)
x = Dense(10000, activation="linear")(x)
output = Dense(10000, activation="softmax")(x)

n_network = Model(input_img, output)
n_network.compile("adam", loss='mae')
n_network.save('googlenet-imp.h5')
