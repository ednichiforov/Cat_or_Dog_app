import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
img_width = 224
img_height = 224


def load_image(img_path):
    img = image.load_img(img_path, target_size=(img_width, img_height))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    return img_tensor


model = tf.keras.models.load_model("/Users/ednichiforov/Python/Web+ML/TEST")

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

img_path = '/Users/ednichiforov/Python/Web+ML/uploads/images/dog.12488.jpg'

new_image = load_image(img_path)

pred = model.predict(new_image)

if pred[0][0] == 1:
    print("dog")
else:
    print("cat")
