import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Cargar imagen y convertir a np
image_path = 'astronauta.png'
original_image = Image.open(image_path).convert('RGBA')
resized_image = original_image.resize((50, 50))
np_image = np.array(resized_image)

# Crear la gráfica

WIDTH = 800
HEIGHT = 600
fig = plt.figure(figsize=(WIDTH/100, HEIGHT/100), dpi=100)
ax = fig.add_subplot([0,0,1,1])
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_aspect('equal')

position = [50, 50]
image_plot = ax.imshow(np_image, extent=(position[0], position[0] + 50, position[1], position[1] + 50), zorder=1)
fig.canvas.draw()

plt.show()

"""
# Cargar imagen y convertir a np
image_path = 'astronauta.png'
image = Image.open(image_path)
image = image.resize((50, 50))
image = np.array(image)

# Crear la imagen
fig, ax = plt.subplots()
plt.show()

"""