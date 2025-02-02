"""
Tests for Perlin noise generator function.

Tests cover:
- Output dimensions match input parameters
- Invalid parameters are handled correctly
"""

import unittest
import numpy as np
from noise import pnoise2

def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed):
    """Generate a 2D array of Perlin noise with the given parameters."""
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

class TestPerlinNoiseGenerator(unittest.TestCase):
    def setUp(self):
        """Set up default test parameters"""
        self.width = 64
        self.height = 48
        self.scale = 0.1
        self.octaves = 6
        self.persistence = 0.5
        self.lacunarity = 2.0
        self.seed = 42

    def test_output_shape(self):
        """Check if output array has correct dimensions"""
        noise = generate_perlin_noise(
            self.width, self.height, self.scale, 
            self.octaves, self.persistence, 
            self.lacunarity, self.seed
        )
        self.assertEqual(noise.shape, (self.height, self.width))


    def test_invalid_parameters(self):
        """Check if invalid parameters raise appropriate errors"""
        with self.assertRaises(ValueError):
            generate_perlin_noise(
                -1, self.height, self.scale,
                self.octaves, self.persistence,
                self.lacunarity, self.seed
            )

if __name__ == '__main__':
    unittest.main()