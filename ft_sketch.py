import numpy as np
import matplotlib.pyplot as plt

# Image dimensions
M, N = 32, 32

# Frequency pairs (u, v)
freq_pairs = [(0, 0), (0, 8), (0, 16), (0, 24)]

x = np.arange(M)
y = np.arange(N)
X, Y = np.meshgrid(x, y)

# Set up the plot
fig, axs = plt.subplots(1, 4, figsize=(16, 4))

for idx, (u, v) in enumerate(freq_pairs):
    # Calculate the real part: cos(2π * (xu/M + yv/N))
    # Since u=0, simplifies to cos(2π * yv/N)
    real_part = np.cos(2 * np.pi * (X * u / M + Y * v / N))
    
    # Plot the image
    ax = axs[idx]
    im = ax.imshow(real_part, cmap='gray', vmin=-1, vmax=1)
    ax.set_title(f'(u, v) = ({u}, {v})')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()