#from typing_extensions import runtime

import math
from typing_extensions import runtime
from PIL import UnidentifiedImageError
from manim import *
# How to compile Manim: CMD -> manim -pql scene.py OurFunctionF

## Example: SineCurveUnitCircle  - may be better

class OurFunctionF(Scene):
    def construct(self):
        equation = MathTex(
            "F(x)", "=", "\\int_{1}^x \\frac{1}{t} dt"
        )
        equation.set_color(YELLOW)
        equation.move_to(UP * 3 + LEFT * 3)
        x_tracker = ValueTracker(1.8)
        ax = Axes(
                x_range=[0, 10],
                y_range=[0, 1.5],
                x_axis_config={"numbers_to_include": [1]},
                tips=False,
            )

        labels = ax.get_axis_labels()

        curve = ax.get_graph(lambda x: 1/x , x_range=[0.8, 10], color=BLUE_C)
        x_AXIS = ax.get_graph(lambda x: 0, x_range=[0,10], color= WHITE)
        curve_label = ax.get_graph_label(
            curve, "\\frac{1}{t}", x_val=1.5, direction=UP * 7
        )
        line_1 = ax.get_vertical_line(ax.input_to_graph_point(1, curve), color=YELLOW)


        # Here Starts the cool code.

        line_moving = always_redraw(
            lambda: ax.get_vertical_line(ax.i2gp(x_tracker.get_value(), curve), color=YELLOW)
            )
        # line_ref = line_moving.copy

        area = always_redraw(lambda: ax.get_area(curve, [1, x_tracker.get_value()], bounded=x_AXIS, color=GREY, opacity=0.2))
        
        function_value_text = (
            Tex("F(")
            .next_to(area, RIGHT * 2 + UP , buff= 0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )
        x_value = always_redraw (
            lambda: DecimalNumber(num_decimal_places= 1)
            .set_value(x_tracker.get_value())
            .next_to(function_value_text,RIGHT, buff= 0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()
        x_value_copy = always_redraw (
            lambda: DecimalNumber(num_decimal_places= 1)
            .set_value(x_tracker.get_value())
            .next_to(line_moving,DOWN, buff= 0.1)
            .set_color(WHITE)
        ).add_background_rectangle()
        function_value_text2 = always_redraw(
            lambda:(Tex(")=")
            .next_to(x_value, RIGHT, buff= 0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
            )
        )
        function_value = always_redraw (
            lambda: DecimalNumber(num_decimal_places= 3)
            .set_value(math.log(x_tracker.get_value()))
            .next_to(function_value_text2,RIGHT, buff= 0.1)
            .set_color(YELLOW)
        ).add_background_rectangle()
        
        
        self.play(Write(equation))
        self.play(Create(ax), Create(labels))
        self.play(Create(curve), Create(curve_label))
        self.wait()
        self.add(function_value_text,x_value,function_value_text2, x_value_copy ,function_value)
        self.play(Create(line_1),Create(line_moving),Create(area))

        self.wait()
        self.play(x_tracker.animate.set_value(5), runtime = 15, rate_func = linear)
        self.wait(1)
        self.play(x_tracker.animate.set_value(1), runtime = 5, rate_func = linear)
        self.wait(1)
        self.play(x_tracker.animate.set_value(2.8), runtime = 15, rate_func = linear) 
        self.wait(1)


class AdditiveProperty(Scene):
    def construct(self):
        equation = MathTex(
            "F(x)", "=", "\\int_{1}^x \\frac{1}{t} dt"
        )
        equation_property = MathTex(
            "F(x_1 \\cdot x_2)", "=", "F(x_1)", "+", "F(x_2)"
        )
        equation_x_2_O = MathTex(
            "F(x_1)", "=", "\\int_{1}^{x_1} \\frac{1}{t} dt", 
        )
        equation_x_2_I = MathTex(
            "F(x_2)", "=", "\\int_{1}^{x_2} \\frac{1}{t} dt", 
        )
        equation_x_2_II = MathTex(
            "F(x_2)", "=", "\\int_{1}^{x_2} \\frac{1}{t} dt", "\\quad", "r = x_1 \\cdot t"
        )
        equation_x_2_III = MathTex(
            "F(x_2)", "=", "\\int_{x_1}^{x_1 \\cdot x_2} \\frac{x_1}{r} \cdot \\frac{1}{x_1} dr", "\\quad", "r = x_1 \\cdot t"
        )
        equation_x_2_IV = MathTex(
            "F(x_2)", "=", "\\int_{x_1}^{x_1 \\cdot x_2} \\frac{1}{r} dr", 
        )
        equation_x_2_V = MathTex(
            "F(x_1) + F(x_2)", "=", "\\int_{1}^{x_1} \\frac{1}{r} dr", "+", "\\int_{x_1}^{x_1 \\cdot x_2} \\frac{1}{r} dr", 
        )
        equation.set_color(YELLOW)
        equation.move_to(UP * 3 + LEFT * 3)
        equation_property.set_color(YELLOW)
        equation_property.move_to(UP * 3 + RIGHT * 3)
        framebox = SurroundingRectangle(equation_property)
        framebox.set_color(WHITE)
        ax = Axes(
                x_range=[0, 10],
                y_range=[0, 1.5],
                x_axis_config={"numbers_to_include": [1]},
                tips=False,
            )

        labels = ax.get_axis_labels()

        curve = ax.get_graph(lambda x: 1/x , x_range=[0.8, 10], color=BLUE_C)
        x_AXIS = ax.get_graph(lambda x: 0, x_range=[0,10], color= WHITE)
        # curve_label = ax.get_graph_label(curve, "\\frac{1}{t}", x_val=1.5, direction=UP * 7)
        line_1 = ax.get_vertical_line(ax.input_to_graph_point(1, curve), color=YELLOW)
        x_1 = 2.5
        x_2 = 3.5
        line_x1 = ax.get_vertical_line(ax.input_to_graph_point(x_1, curve), color=YELLOW)
        x_1_value = MathTex('x_1').next_to(line_x1,DOWN, buff= 0.1).set_color(WHITE)
        line_x2 = ax.get_vertical_line(ax.input_to_graph_point(x_2, curve), color=YELLOW)
        x_2_value = MathTex('x_2').set_value(x_2).next_to(line_x2,DOWN, buff= 0.1).set_color(WHITE)
        line_x3 = ax.get_vertical_line(ax.input_to_graph_point(x_1 * x_2, curve), color=YELLOW)
        x_3_value = MathTex('x_1 \\cdot x_2').set_value(x_1 * x_2).next_to(line_x3,DOWN, buff= 0.1).set_color(WHITE)
        area_1 = ax.get_area(curve, [1, x_1], bounded=x_AXIS, color=GREEN, opacity=0.2)
        area_2 = ax.get_area(curve, [1, x_2], bounded=x_AXIS, color=GREY, opacity=0.2)
        area_3 = ax.get_area(curve, [x_1, x_1*x_2], bounded=x_AXIS, color=GREY, opacity=0.2)
        area_1_copy = ax.get_area(curve, [1, x_1], bounded=x_AXIS, color=GREEN, opacity=0.2)

        self.add(equation, ax, curve, line_1)
        self.wait()
        self.play(Create(framebox),Write(equation_property))
        self.wait()
        self.play(Create(line_x1),Create(x_1_value), Create(area_1), Write(equation_x_2_O))
        self.wait(0.5)
        self.play(Create(line_x2), Create(x_2_value), Create(area_2),FadeOut(equation_x_2_O), Uncreate(area_1), Write(equation_x_2_I))
        self.wait()
        self.play(ReplacementTransform(equation_x_2_I,equation_x_2_II))
        self.wait()
        self.play(ReplacementTransform(equation_x_2_II,equation_x_2_III),Create(line_x3),Create(x_3_value))
        self.play(ReplacementTransform(area_2,area_3))
        self.wait()
        self.play(ReplacementTransform(equation_x_2_III,equation_x_2_IV))
        self.wait()
        self.play(ReplacementTransform(equation_x_2_IV,equation_x_2_V),Create(area_1_copy))
        self.wait()

class Similarity_to_log(Scene):
    def construct(self):
        equation = MathTex(
            "F(x)", "=", "\\int_{1}^x \\frac{1}{t} dt"
        )
        equation_property = MathTex(
            "F(x_1 \\cdot x_2)", "=", "F(x_1)", "+", "F(x_2)"
        )
        equation.set_color(YELLOW)
        equation.move_to(UP * 3 + LEFT * 3)
        equation_property.set_color(YELLOW)
        equation_property.move_to(UP * 3 + RIGHT * 3)
        framebox = SurroundingRectangle(equation_property)
        framebox.set_color(WHITE)
        ax = Axes(
                x_range=[0.5, 10],
                y_range=[-2, 5],
                x_axis_config={"numbers_to_include": []},
                tips=False,
            )
        labels = ax.get_axis_labels()
        
        base_traker = ValueTracker(2)
        func = lambda a: lambda x: (math.log(x)/math.log(a))
        graph = VMobject()
        graph_kwargs = {"color": BLUE}
        # SETUP FORMULA
        decimal = DecimalNumber(base_traker.get_value()).add_updater(lambda v: v.set_value(base_traker.get_value()))
        formula = Tex("y = ", "log(x)/log(", ")")
        # ---- Arrange position of formula
        formula.next_to(ax, DOWN)
        formula.shift(UP)
        formula[2].shift(RIGHT * 0.8)
        decimal.next_to(formula[1],RIGHT*0.25)
        # SET UPDATERS
        def update_graph(mob):
            mob.become(
                ax.get_graph(
                    func(base_traker.get_value()),
                    **graph_kwargs
                )
            )
        # SET INITIAL STATE OF GRAPH
        update_graph(graph)
        graph.add_updater(update_graph)
        self.add(equation,equation_property,framebox)
        self.wait(1)
        self.play(Create(ax),Write(labels))
        self.wait(1)
        self.play(Create(graph),Write(VGroup(formula[0],formula[1],decimal, formula[2])))
        self.play(
            base_traker.animate.set_value(9.9), runtime = 15, rate_functions = linear
        )
        self.wait(1)
        self.play(
            base_traker.animate.set_value(1.7), runtime = 15, rate_functions = linear
        )
        self.wait(1)
        self.play(
            base_traker.animate.set_value(2.8), runtime = 15, rate_functions = linear
        )
        self.wait()






class SumGeometricSeries(Scene):
    def construct(self):
        geometric_sum = MathTex(
            "1", "+", "\\frac{1}{2}", "+", "\\frac{1}{4}", "+" ,"\\frac{1}{8}", "+ \cdots"
        )
        geometric_sum.shift(UP* 3 + LEFT * 4)
        frameboxes = [SurroundingRectangle(geometric_sum[2*i], buff = .1) for i in range(4)]
        SideUnit = 3.0
        rectangles = [Rectangle(height= SideUnit * (1/2)**((i+1) // 2), width= SideUnit * (1/2)**(i // 2), fill_opacity = 0.9-i*0.08, color= YELLOW) for i in range(20)]
        Location = LEFT * (SideUnit/2)
        
        


        self.play(Write(geometric_sum))
        self.play(
            Create(frameboxes[0]),
        )
        
        
        for i in range(3):
            rectangles[i].move_to(Location)
            self.play(
                TransformFromCopy(frameboxes[i],rectangles[i])
            )
            if i % 2 == 0:
                Location += (RIGHT * SideUnit + DOWN * (SideUnit/4)) *((1/2)**(i/2))
            else:
                Location += (UP * (SideUnit/2) + LEFT * (SideUnit/4))* ((1/2)**((i-1)/2))

            self.wait()
            self.play(
                ReplacementTransform(frameboxes[i],frameboxes[i+1]),
            )
        rectangles[3].move_to(Location)
        self.play(
            TransformFromCopy(frameboxes[3],rectangles[3])
        )
        Location += (UP * (SideUnit/2) + LEFT * (SideUnit/4))* ((1/2)**((3-1)/2))

        self.wait()

        for i in range(4,len(rectangles)):
            rectangles[i].move_to(Location)
            self.play(
                Create(rectangles[i])
            )
            if i % 2 == 0:
                Location += (RIGHT * SideUnit + DOWN * (SideUnit/4)) *((1/2)**(i/2))
            else:
                Location += (UP * (SideUnit/2) + LEFT * (SideUnit/4))* ((1/2)**((i-1)/2))
        self.wait()
        

class HarmonicSeriesToFunction(Scene):
    def construct(self):
        harmonic_sum_equation = MathTex(
            r"1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \cdots"
        )
        harmonic_sum_equation.set_color(YELLOW)
        harmonic_sum_equation.move_to(UP * 3)
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 1.5],
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve = ax.get_graph(lambda x: 1/x , x_range=[0.8, 10], color=BLUE_C)
        curve_label = ax.get_graph_label(
            curve, "\\frac{1}{x}", x_val=1.5, direction=UP * 7
        )

        area_1 = ax.get_area(curve, x_range=[1, 9], dx_scaling=500, color=YELLOW)
        self.wait(1)
        self.play(Create(harmonic_sum_equation))
        self.wait(1)
        self.play(TransformFromCopy(harmonic_sum_equation,area_1))
        self.wait(1)
        self.play(FadeIn(ax), FadeIn(labels))
        self.wait(0.5)
        self.play(Create(curve), FadeIn(curve_label))
        self.wait(1)