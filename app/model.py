from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Charger le modèle ResNet50 pré-entraîné
model = ResNet50(weights='imagenet')

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    # Décoder les prédictions
    results = decode_predictions(preds, top=5)[0]
    # Formater les résultats
    return [{"label": res[1], "probability": float(res[2])} for res in results]
