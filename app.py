import numpy as np
import cv2
from tensorflow import keras

# Charger le modèle
model = keras.models.load_model("breast_cancer_model.keras")

# Fonction pour prédire une nouvelle image
def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict(img)
    if prediction[0] > 0.5:
        return "Malignant"
    else:
        return "Benign"

# Exemple d'utilisation
if __name__ == "__main__":
    image_path = "./try/A1.JPG"  # Chemin de l'image dans le conteneur
    result = predict_image(image_path)
    print(f"La prédiction pour l'image est : {result}")
