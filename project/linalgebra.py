#this code has an error on line 14, going to continue with manim tutorial before i come back to this

from manim import *

class LinearAlgebraScene(Scene):
    def construct(self):
        # Create number plane
        plane = NumberPlane()
        self.add(plane)

        # Create vectors
        vector1 = np.array([-1, 2])  # Adjusted to 2D vector
        vector2 = np.array([3, -1])  # Adjusted to 2D vector

        # Add vectors to the scene
        vector1_mobject = self.get_vector_mobject(vector1, color=RED)
        vector2_mobject = self.get_vector_mobject(vector2, color=BLUE)
        self.play(Create(vector1_mobject), Create(vector2_mobject))

        # Add vector addition
        result_vector = self.get_vector_mobject(vector1 + vector2, color=GREEN)
        self.play(TransformFromCopy(vector1_mobject, result_vector))
        self.play(TransformFromCopy(vector2_mobject, result_vector))

        # Add scalar multiplication
        scalar = 2
        scaled_vector = self.get_vector_mobject(scalar * vector1, color=YELLOW)
        self.play(TransformFromCopy(vector1_mobject, scaled_vector))
        self.play(ApplyMethod(scaled_vector.shift, vector2))

        self.wait(2)

    def get_vector_mobject(self, vector, **kwargs):
        return Line(ORIGIN, vector[:2], **kwargs)

