from manim import *

class DotProductScene(Scene):
    def construct(self):
        # Create number plane
        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5])
        self.add(plane)

        # Create vectors
        vector1 = Vector([3, 1], color=RED)
        vector2 = Vector([2, 2], color=BLUE)

        # Add vectors to the scene
        self.play(Create(vector1), Create(vector2))

        # Calculate dot product
        dot_product = np.dot(vector1.get_end(), vector2.get_end())

        # Add dot product label
        dot_product_label = MathTex(r"\text{Dot Product:}", r"3 \cdot 2 + 1 \cdot 2 =", str(dot_product))
        dot_product_label.next_to(vector1.get_end(), direction=RIGHT)
        self.play(Write(dot_product_label))

        # Highlight the dot product calculation
        self.play(ApplyMethod(dot_product_label[-1].set_color, YELLOW))

        self.wait(2)
