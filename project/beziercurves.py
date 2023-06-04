from manim import *

class BezierCurvesScene(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=(-1.5, 1.5),
            y_range=(-1.5, 1.5),
            x_length=6,
            y_length=6,
            axis_config={"include_tip": True}
        )
        self.play(Create(axes))

        # Create control points
        control_points = [
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 1.5, 0],
            [1, 1, 0],
            [1, -1, 0],
            [0, -1.5, 0]
        ]

        # Create Bézier curves
        bezier_curves = []
        for i in range(2, 7):
            bezier_curve = self.get_bezier_curve(control_points[:i])
            bezier_curves.append(bezier_curve)
            self.play(Create(bezier_curve))

        self.wait(2)

    def get_bezier_curve(self, control_points):
        curve = VMobject() #Where our curves are instantiated
        curve.set_points_smoothly([*control_points, control_points[0]])
        return curve
