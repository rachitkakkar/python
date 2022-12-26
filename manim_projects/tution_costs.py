from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class TutionCosts3(Scene):
    def construct(self):
        title = Text("Average Cost of Tuition for All Institutions (US $) 1963-2012", font_size=30)
        ax = Axes(
            x_range=[1963, 2012, 7], y_range=[200, 11000, 1200], axis_config={"include_tip": False}
        ).add_coordinates()
        cost = [508,530,549,574,588,596,645,688,724,759,796,809,829,924,984,1073,1163,1289,1457,1626,1783,1985,2181,2312,2458,2658,2839,3016,3286,3517,3827,4044,4338,4564,4755,5013,5222,5377,5646,6002,6608,7122,7601,8092,8483,8893,9136,9598,10180,10683]
        years = []
        for i in range(1963, 2013):
            years.append(i)
        graph = ax.plot_line_graph(x_values=years, y_values=cost, line_color=GREEN, vertex_dot_radius=0.045)
        title.next_to(ax, UP)
        line = ax.get_vertical_line(ax.coords_to_point(1965, 11000), color=YELLOW)
        label = Text("The US\nHigher Education Act\nis passed", font_size=16)
        label.next_to(line)

        self.play(Write(title))
        self.wait(duration=0.25)
        self.play(Create(ax))
        self.wait(duration=0.25)
        self.play(FadeIn(graph))
        self.wait(duration=0.25)
        
        self.play(Create(line))
        self.play(Create(label))

        self.wait(duration=2)
        self.play(FadeOut(line))
        self.play(FadeOut(label))
        self.play(FadeOut(title))
        self.play(FadeOut(ax))
        self.play(FadeOut(graph))

        message = MarkupText(f'Tuition has gone up by <span fgcolor="{RED}">roughly 3,800 percent</span> since the mid 1960s,\nwhen <span fgcolor="{GREEN}">the US Higher Education Act</span> was passed.', font_size=35)
        message2 = MarkupText(f'The Federal Government owns roughly <span fgcolor="{RED}">$1.3 trillion</span> of the\n<span fgcolor="{GREEN}">$1.6 trillion</span> dollars of student debt.', font_size=35)
        message3 = MarkupText(f'''If you liked that video, make sure to <span fgcolor="{RED}">like and subscribe.</span>\n<span fgcolor="{GREEN}">Comment</span> suggestions for data down below!''', font_size=35)

        self.play(Write(message))
        self.wait(duration=2.5)
        self.play(Transform(message, message2))
        self.wait(duration=2.5)
        self.play(Transform(message, message3))
        self.wait()
