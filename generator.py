
import numpy as np
import psutil
import matplotlib.pyplot as plt
import noise
from noise import pnoise2

# DEVICE RESOLUTION (MODIFY THIS ACCORDING TO YOUR DEVICE)
# ========================================================
DEFAULT_WIDTH = 2560  # Default width for the wallpaper
DEFAULT_HEIGHT = 1440  # Default height for the wallpaper
# ========================================================

# WALLPAPER AND OUTLINE COLORS
# ========================================================
DEFAULT_COLOR = "#858585"  # Default color for contour lines (white in hex)
DEFAULT_BG_COLOR = "#000000"  # Default background color (black in hex)
# ========================================================

# PERLIN NOISE PARAMETERS
DEFAULT_SCALE = 0.002  # Scale for Perlin noise
DEFAULT_OCTAVES = 4  # Octaves for Perlin noise
DEFAULT_PERSISTENCE = 0.5  # Persistence for Perlin noise
DEFAULT_LACUNARITY = 2.0  # Lacunarity for Perlin noise
DEFAULT_DPI = 300  # DPI for saving the image
DEFAULT_CONTOUR_LEVELS = 10  # Number of contour levels

def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed):
    ''' Generate Perlin noise based on parameters and seed '''
    noise_data = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            # storing perlin noise for each pixel with the parameters
            noise_data[i][j] = pnoise2(j * scale,i * scale,octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=width,repeaty=height,base=seed)
    return noise_data

def normalize_data(data):
    """Normalize the data to the range [0, 1]."""
    # I see you, reading my code!
    # basic min max normalization stuff, nothing too complicated!
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def generate_wallpaper(width, height, color=DEFAULT_COLOR, bgcolor=DEFAULT_BG_COLOR, scale=DEFAULT_SCALE,octaves=DEFAULT_OCTAVES, persistence=DEFAULT_PERSISTENCE, lacunarity=DEFAULT_LACUNARITY,contour_levels=DEFAULT_CONTOUR_LEVELS, dpi=DEFAULT_DPI):
    ''' Generate a procedural wallpaper using Perlin noise and contour lines.'''
    # Use CPU utilization as a unique seed for Perlin noise (personal touch)
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_usage = max(0, min(cpu_usage, 100))
    seed = int(cpu_usage * 10)  # Scale it reasonably (e.g., 0-1000 range)
    # I didn't have the above code, and I literally crashed my computer for some reason (lmao)


    # This is where we're extracting the noise data for each pixel
    noise_data = generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed)
    noise_data = normalize_data(noise_data)

    # This is where I'm plotting the contour lines
    plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    levels = np.linspace(0.2, 0.8, contour_levels)
    plt.contour(noise_data, levels=levels, colors=color, linewidths=0.5)
    plt.axis("off")
    plt.gca().set_facecolor(bgcolor)

    # Finally!, saving the image
    output_filename = f"procedural_wallpaper_{seed}.png"
    plt.savefig(output_filename, bbox_inches="tight", pad_inches=0, dpi=dpi, facecolor=bgcolor)
    plt.close()

    #Displaying the noise pattern generated at that specific CPU usage for that sepcific moment (that's a lot of specifics)
    print(f"Wallpaper generated with CPU usage seed: {seed}%")
    return output_filename


if __name__ == "__main__":
    # main function (don't judge my code)
    generate_wallpaper(DEFAULT_WIDTH, DEFAULT_HEIGHT, color=DEFAULT_COLOR, bgcolor=DEFAULT_BG_COLOR)