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
        dot_product_value = np.dot(vector1.get_end(), vector2.get_end())
        dot_product = DecimalNumber(dot_product_value, num_decimal_places=2)
        dot_product.next_to(vector1.get_end(), direction=DOWN, buff=0.2)
        self.play(Write(dot_product))

        # Add dot product label
        dot_product_label = MathTex(r"\text{Dot Product:}")
        dot_product_label.next_to(dot_product, direction=UP, buff=0.2)
        self.play(Write(dot_product_label))

        # Highlight the dot product calculation
        self.play(ApplyMethod(dot_product.set_color, YELLOW))

        self.wait(2)
        
