import os
from pathlib import Path
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'


def make_prediction(image_path):
    class_names = ["cat", "dog"]
    img_width = 224
    img_height = 224

    model_path = Path("Mymodel")
    model = load_model(model_path)
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    img = image.load_img(image_path, target_size=(img_width, img_height))
    input_arr = image.img_to_array(img)
    img_np = np.expand_dims(input_arr, axis=0)
    img_tensor = img_np/255.

    prediction = model.predict_classes(img_tensor)

    return class_names[prediction[0][0]]
