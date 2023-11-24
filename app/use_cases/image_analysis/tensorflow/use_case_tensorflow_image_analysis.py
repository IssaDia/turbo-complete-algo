from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from interfaces.image_analysis_interface import ImageUseCase
import numpy as np

model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))

class TensorFlowImageUseCase(ImageUseCase):
    def analyze_image(self, image_path: str) -> str:
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Return the top predicted classes and their probabilities
        return [(label, prob) for (_, label, prob) in decoded_predictions]