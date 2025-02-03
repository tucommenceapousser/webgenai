from PIL import ImageDraw, ImageFont
import numpy as np
import cv2

def add_watermark(image, text="trhacknon"):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    
    # Générer une police type "alien" (ajuster selon besoin)
    font = ImageFont.load_default()
    
    # Ajouter le texte en bas à droite (faible opacité)
    position = (width - 150, height - 50)
    draw.text(position, text, fill=(0, 255, 0, 50), font=font)  # Faible opacité
    
    # Convertir l’image pour cacher le filigrane en bruit visuel
    image_np = np.array(image)
    noise = np.random.randint(0, 50, image_np.shape, dtype='uint8')
    image_np = cv2.add(image_np, noise)
    
    return Image.fromarray(image_np)
