from PIL import Image
import numpy as np
from scipy.fftpack import dct, idct
import os

def compress_image(image_path, quality):
    image = Image.open(image_path)
    image = image.convert('L')
    dct_image = np.asarray(image).astype(float)
    dct_image = dct(dct_image, axis=0, norm='ortho')
    dct_image = dct(dct_image, axis=1, norm='ortho')
    dct_image /= quality
    idct_image = idct(idct(dct_image, axis=0, norm='ortho'), axis=1, norm='ortho')
    idct_image = np.clip(idct_image, 0, 255)
    idct_image = idct_image.round().astype(np.uint8)
    compressed_image = Image.fromarray(idct_image)
    return compressed_image

def decompress_image(compressed_image_path, output_path):
    compressed_image = Image.open(compressed_image_path)
    idct_image = np.asarray(compressed_image).astype(float)
    idct_image = idct(idct_image, axis=0, norm='ortho')
    idct_image = idct(idct_image, axis=1, norm='ortho')
    idct_image = np.clip(idct_image, 0, 255)
    idct_image = idct_image.round().astype(np.uint8)
    decompressed_image = Image.fromarray(idct_image)
    decompressed_image.save(output_path)

image_path = 'jordan.jpeg'
compressed_image_path = 'imagem_comprimida.jpg'
output_path = 'imagem_descomprimida.jpg'
quality = 10

compressed_image = compress_image(image_path, quality)
compressed_image.save(compressed_image_path)

decompress_image(compressed_image_path, output_path)

original_size = os.path.getsize(image_path)
compressed_size = os.path.getsize(compressed_image_path)
decompressed_size = os.path.getsize(output_path)

print("Tamanho da imagem original (em bytes):", original_size)
print("Tamanho da imagem comprimida (em bytes):", compressed_size)
print("Tamanho da imagem descomprimida (em bytes):", decompressed_size)
