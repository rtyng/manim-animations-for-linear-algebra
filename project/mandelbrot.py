from manim import *

class MandelbrotZoomScene(ZoomedScene):
    def setup(self):
        self.zoom_factor = 0.1  # Amount of zoom per step
        self.zoomed_display_height = 3
        self.zoomed_display_width = 4.8  # Adjust the width based on desired aspect ratio
        self.image_resolution = 500
        self.max_iterations = 100

    def construct(self):
        # Parameters for the Mandelbrot fractal
        x_min, x_max = -2.5, 1.0
        y_min, y_max = -1.5, 1.5

        # Create a grid of pixels
        x_range = np.linspace(x_min, x_max, self.image_resolution)
        y_range = np.linspace(y_min, y_max, self.image_resolution)
        pixels = np.zeros((self.image_resolution, self.image_resolution))

        # Calculate Mandelbrot set
        for i, x in enumerate(x_range):
            for j, y in enumerate(y_range):
                c = x + y * 1j
                z = 0
                iteration = 0

                while abs(z) <= 2 and iteration < self.max_iterations:
                    z = z*z + c
                    iteration += 1

                pixels[j, i] = iteration

        # Create image from pixel data
        image = ImageMobject(pixels)
        image.set_height(6)
        color_gradient = [BLUE, GREEN, YELLOW, ORANGE, RED]
        intensity_factor = 5  # Adjust the intensity of the colors
        bright_color_gradient = [intensity_factor * color for color in color_gradient]
        image.set_color_gradient(bright_color_gradient)

        # Set up zoomed camera
        self.setup()
        self.camera.frame.save_state()
        self.zoomed_camera.set_frame_height(self.zoomed_display_height)
        self.zoomed_camera.set_frame_width(self.zoomed_display_width)

        # Display the Mandelbrot fractal with a fade-in animation
        self.add(image)
        self.play(FadeIn(image))

        # Zoom into the fractal
        self.activate_zooming()

        self.wait()
