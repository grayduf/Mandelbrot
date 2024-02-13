import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z * z + c
    return abs(z) <= 2

c = complex_matrix(-2.5, 0.5, -1.5, 1.5, pixel_density=512)

image = Image.fromarray(~is_stable(c, num_iterations=20))
image.show()