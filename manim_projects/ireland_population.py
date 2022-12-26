from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class IrelandShort2(Scene):
    def construct(self):
        years = []
        for i in range(1821, 1911, 10):
            years.append(i)
        years.append(1911)
        years.append(1926)
        years.append(1936)
        years.append(1946)
        for i in range(1950, 2023):
            years.append(i)

        value = [5.41, 6.2, 6.53, 5.11, 4.4, 4.05, 3.87, 3.47, 3.22, 3.14, 2.97, 2.97, 2.96, 2.912680, 2.912608, 2.909051, 2.901318,
        2.889280, 2.873415, 2.854777, 2.835057, 2.816351, 2.801091, 2.791397, 2.788531, 2.792374, 2.801184, 2.812224, 2.823650, 2.834682, 2.846347, 2.860727,
        2.880764, 2.908421, 2.944088, 2.986566, 3.034319, 3.085156, 3.137176, 3.189865, 3.242768, 3.294161, 3.342005, 3.384756, 3.422018, 3.453786, 3.479458, 3.498530,
        3.510979, 3.516422, 3.515828, 3.512185, 3.509519, 3.510885, 3.517710, 3.529853, 3.546931, 3.567912, 3.592186,
        3.619641, 3.651096, 3.687819, 3.731468, 3.783103, 3.842245, 3.907998, 3.980076, 4.058130, 4.141223, 4.230623, 4.324641, 4.415872, 4.494576, 4.554321, 4.591105, 4.608198, 4.615422, 4.626844, 4.652425, 4.695779, 4.753279, 4.882495, 4.937786, 4.982907, 5.020199]
        ax = Axes(
            x_range=[1821, 2022, 20], y_range=[2, 7, 1], axis_config={"include_tip": False}
        ).add_coordinates()
        graph = ax.plot_line_graph(x_values=years, y_values=value, line_color=GREEN, vertex_dot_radius=0)
        title = Text("Population of Ireland from 1821-2022 (in millions)", font_size=30)
        title.next_to(ax, UP)

        label = Text(".\n\n\n\n\nStart of\nthe Irish\nPotato Famine", font_size=15)
        label2 = Text("Start of\nIrish War\nof Independence", font_size=15)
        label3 = Text("Ireland\nBecomes\nIndependent\nfrom Britian", font_size=15)

        line = ax.get_vertical_line(ax.coords_to_point(1845, 7), color=YELLOW)
        line2 = ax.get_vertical_line(ax.coords_to_point(1919, 7), color=YELLOW)
        line3 = ax.get_vertical_line(ax.coords_to_point(1922, 7), color=YELLOW)

        message = MarkupText(f'The Irish Potato Famine led to at least <span fgcolor="{RED}">a million deaths</span>\nand <span fgcolor="{RED}">another million</span> emmigrated to other countries.', font_size=35)
        message2 = MarkupText(f'''Around <span fgcolor="{RED}"> 9 to 10 million</span> people born in Ireland have emigrated,\ngreater than the country's population.''', font_size=35)
        message3 = MarkupText(f'''In 1890,  <span fgcolor="{RED}">40%</span> of Irish-born people were living abroad.''', font_size=35)
        message4 = MarkupText(f'''Ireland has yet to reach the peak population of <span fgcolor="{RED}">6.5 million</span>\npre-famine. The current population is <span fgcolor="{GREEN}">around 5 million.</span>''', font_size=35)
        message5 = MarkupText(f'''If you liked that video, make sure to <span fgcolor="{RED}">like and subscribe.</span>\n<span fgcolor="{GREEN}">Comment</span> suggestions for data down below!''', font_size=35)

        label.next_to(line, RIGHT)
        label2.next_to(line2, LEFT)
        label3.next_to(line3, RIGHT)

        self.play(Write(title))
        self.wait(duration=0.25)
        self.play(Create(ax))
        self.wait(duration=0.25)
        self.play(FadeIn(graph))
        self.wait(duration=0.25)

        self.play(Create(line))
        self.play(Create(label))
        self.play(Create(line2))
        self.play(Create(label2))
        self.play(Create(line3))
        self.play(Create(label3))
        self.wait(duration=0.25)

        self.play(FadeOut(line))
        self.play(FadeOut(label))
        self.play(FadeOut(line2))
        self.play(FadeOut(label2))
        self.play(FadeOut(line3))
        self.play(FadeOut(label3))

        self.play(FadeOut(title))
        self.play(FadeOut(ax))
        self.play(FadeOut(graph))

        self.play(Write(message))
        self.wait(duration=3.5)
        self.play(Transform(message, message2))
        self.wait(duration=3.5)
        self.play(Transform(message, message3))
        self.wait(duration=3.5)
        self.play(Transform(message, message4))
        self.wait(duration=3.5)
        self.play(Transform(message, message5))

        self.wait()