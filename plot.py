import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class GazeVisualizer:
    def __init__(self):
        # Create a black screen
        self.fig, self.ax = plt.subplots()
        self.ax.set_facecolor('black')
        self.ax.set_xlim(-5, 5)  # Adjust the limits as needed based on your screen size
        self.ax.set_ylim(-5, 5)

        # Initialize the circle representing gaze
        self.circle = plt.Circle((0, 0), radius=1, color='white', fill=False)
        self.ax.add_artist(self.circle)

        # Create an animation that updates the plot every 100 milliseconds
        self.ani = FuncAnimation(self.fig, self.update, blit=True, interval=50)

        # Set plot properties
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')

    def update(self, x, y):
        # Generate random gaze data for demonstration purposes
        self.circle.set_center((x, y))
        return self.circle,

    def show(self):
        # Show the plot
        plt.show()

