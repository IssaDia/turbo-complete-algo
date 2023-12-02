from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from interfaces.image_analysis_interface import ImageUseCase
import numpy as np

# Utilisation de ResNet50 au lieu de MobileNetV2
model = ResNet50(weights='imagenet', input_shape=(224, 224, 3))

class TensorFlowImageUseCase(ImageUseCase):
    def analyze_image(self, image_path: str) -> str:
        # Traitements de l'image pour correspondre à la forme d'entrée attendue par ResNet50
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Prédiction des probabilités pour chaque classe d'ImageNet
        predictions = model.predict(img_array)
        
        # Décodage des prédictions pour obtenir les trois meilleures classes prédites
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Retourne une liste contenant le nom de la classe et la probabilité associée
        return [(label, prob) for (_, label, prob) in decoded_predictions]
