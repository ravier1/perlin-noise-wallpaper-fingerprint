
import numpy as np
import noise
from noise import pnoise2


def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed):
    """Generate Perlin noise based on the given parameters and seed."""
    noise_data = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            noise_data[i][j] = pnoise2(
                j * scale,
                i * scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=width,
                repeaty=height,
                base=seed
            )
    return noise_data
