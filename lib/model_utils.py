import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "model/v1"

IMAGE_SIZE = (256, 256)
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def prepare_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def predict(model, image_array):
    predictions = model.predict(image_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    
    return predicted_class