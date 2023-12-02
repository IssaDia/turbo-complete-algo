from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Chargement du modèle ResNet50 pré-entraîné avec les poids ImageNet
model = ResNet50(weights='imagenet', input_shape=(224, 224, 3))

def predict_product_category_resnet50(image_path):
    # Chargement de l'image et redimensionnement à la taille attendue par ResNet50
    img = image.load_img(image_path, target_size=(224, 224))
    # Conversion de l'image en tableau numpy
    img_array = image.img_to_array(img)
    # Ajout d'une dimension pour correspondre à la forme d'entrée attendue par le modèle
    img_array = np.expand_dims(img_array, axis=0)
    # Prétraitement de l'image selon les besoins du modèle ResNet50
    img_array = preprocess_input(img_array)

    # Prédiction des probabilités pour chaque classe d'ImageNet
    predictions = model.predict(img_array)
    # Décodage des prédictions pour obtenir les trois meilleures classes prédites
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Retourne une liste de tuples contenant le nom de la classe et la probabilité associée
    return [(label, prob) for (_, label, prob) in decoded_predictions]
