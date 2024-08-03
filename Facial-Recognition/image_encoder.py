from PIL import Image
import numpy as np

def encode_image(image_path: str) -> np.ndarray:
    """Encodes an image into a vector.
    
    Args:
        image_path (str): The path to the image file.

    Returns:
        np.ndarray: The encoded vector of the image.
    """
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to grayscale for simplicity
        img = img.convert('L')
        # Resize the image to a fixed size (e.g., 128x128)
        img = img.resize((128, 128))
        # Convert the image to a numpy array
        img_array = np.array(img)
        # Flatten the image array to create a vector
        img_vector = img_array.flatten()
        return img_vector

