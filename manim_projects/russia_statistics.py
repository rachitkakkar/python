from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class RussiaShort1(Scene):
    def construct(self):
        years = []
        for i in range(1988, 2021):
            years.append(i)
        gdp = [554.71, 506.50, 516.81, 517.96, 460.29, 435.08, 395.08, 395.54, 391.72, 404.93, 270.96, 195.91, 259.71, 306.60, 345.47, 430.35, 591.02, 764.02, 989.93, 1299.71, 1660.85, 1222.64, 1524.92, 2045.93, 2208.30, 2292.47, 2059.24, 1363.48, 1276.79, 1574.20, 1657.33, 1687.45, 1483.50, 1709.58]
        
        ax = Axes(
            x_range=[1988, 2021, 3], y_range=[0, 3000, 1000], axis_config={"include_tip": False}
        ).add_coordinates()
        graph = ax.plot_line_graph(x_values=years, y_values=gdp, line_color=GREEN)

        years = []
        for i in range(1950, 2022):
            years.append(i)
        birth = [27.646, 27.403, 27.161, 26.918, 26.675, 26.675, 26.433, 26.190, 25.948, 25.705, 24.789, 23.872, 22.956, 22.039, 21.123, 19.893, 18.663, 17.432, 16.202, 14.972, 15.052, 15.132, 15.211, 15.291, 15.371, 15.451, 15.531, 15.610, 15.690, 15.770, 15.963, 16.157, 16.350, 16.544, 16.737, 16.625, 16.513, 16.402, 16.290, 16.178, 15.113, 14.048, 12.982, 11.917, 10.852, 10.464, 10.076, 9.688, 9.300, 8.912, 9.092, 9.272, 9.451, 9.631, 9.811, 10.133, 10.455, 10.776, 11.098, 11.420, 11.732, 12.044, 12.357, 12.669, 12.981, 12.939, 12.897, 12.854, 12.812, 12.770, 12.482, 12.194, 11.905, 11.617]
        ax2 = Axes(
            x_range=[1950, 2022, 7], y_range=[5, 30, 5], axis_config={"include_tip": False}
        ).add_coordinates()
        graph2 = ax2.plot_line_graph(x_values=years, y_values=birth, line_color=RED, vertex_dot_radius=0.045)
        
        years = []
        for i in range(1996, 20222):
            years.append(i)
        value = [0.1728, 0.1687, 0.04, 0.0347, 0.0323, 0.0305, 0.0335, 0.034, 0.0353, 0.037, 0.04, 0.041, 0.0335, 0.0323, 0.0323, 0.0305, 0.0311, 0.0167, 0.0138, 0.0156, 0.0167, 0.015, 0.0156, 0.0132, 0.0132, 0.0102, 0.007]
        ax3 = Axes(
            x_range=[1996, 2022, 3], y_range=[0, 0.225, 0.025], axis_config={"include_tip": False}
        ).add_coordinates()
        graph3 = ax3.plot_line_graph(x_values=years, y_values=value, line_color=BLUE)

        title = Text("Rusian GDP (Billions of US $) from 1988-2021", font_size=30)
        title2 = Text("Russia's Birth Rate (Per 1000 People) 1950-2022", font_size=30)
        title3 = Text("Value Of The Russian Ruble (in US $) 1996-2022", font_size=30)
        title.next_to(ax, UP)
        title2.next_to(ax, UP)
        title3.next_to(ax2, UP)
        
        line = ax.get_vertical_line(ax.coords_to_point(1991, 3000), color=YELLOW)
        line2 = ax.get_vertical_line(ax.coords_to_point(1994, 3000), color=YELLOW)
        line3 = ax.get_vertical_line(ax.coords_to_point(2014, 3000), color=YELLOW)
        line4 = ax2.get_vertical_line(ax2.coords_to_point(1991, 30), color=YELLOW)
        line5 = ax2.get_vertical_line(ax2.coords_to_point(1994, 30), color=YELLOW)
        line6 = ax2.get_vertical_line(ax2.coords_to_point(2014, 30), color=YELLOW)
        line7 = ax2.get_vertical_line(ax2.coords_to_point(1957, 30), color=YELLOW)
        line8 = ax2.get_vertical_line(ax2.coords_to_point(1962, 30), color=YELLOW)
        line9 = ax2.get_vertical_line(ax2.coords_to_point(1980, 30), color=YELLOW)
        line10 = ax3.get_vertical_line(ax3.coords_to_point(2014, 0.225), color=YELLOW)
        line11 = ax3.get_vertical_line(ax3.coords_to_point(2022, 0.225), color=YELLOW)

        label = Text("Collapse\nOf  The\nSoviet\nUnion", font_size=15)
        label2 = Text("Russian\nInvasion Of\nChechnya", font_size=15)
        label3 = Text("Russian Annexation\nOf  Crimea\n\n\n\n\n\n.", font_size=16)
        label4 = Text("Collapse\nOf  The\nSoviet\nUnion\n\n\n\n\n.", font_size=14)
        label5 = Text("Russian\nInvasion Of\nChechnya", font_size=14)
        label6 = Text("Russian Annexation\nOf  Crimea", font_size=14)
        label7 = Text("Sputnik I\nIs\nLaunched", font_size=14)
        label8 = Text(".\n\n\n\nCuban\nMissile\nCrisis", font_size=14)
        label9 = Text("The 1980\nSummer\nOlympics", font_size=14)
        label10 = Text("Russian\nAnnexation\nOf  Crimea", font_size=16)
        label11 = Text("Russian Invasion\nOf  Ukraine", font_size=16)

        message = Text("If You Enjoyed This Video, Please Like and Subscribe\nComment suggestions down below!", font_size=45)
        label.next_to(line, RIGHT)
        label2.next_to(line2, RIGHT)
        label3.next_to(line3, RIGHT)

        label4.next_to(line4, LEFT)
        label5.next_to(line5, RIGHT)
        label6.next_to(line6, RIGHT)

        label7.next_to(line7, LEFT)
        label8.next_to(line8, RIGHT)
        label9.next_to(line9, LEFT)

        label10.next_to(line10, RIGHT)
        label11.next_to(line11, LEFT)

        self.play(Write(title))
        self.wait(duration=0.25)
        self.play(Create(ax))
        self.wait(duration=0.25)
        self.play(FadeIn(graph))
        self.play(Create(line))
        self.play(Create(label))
        self.play(Create(line2))
        self.play(Create(label2))
        self.play(Create(line3))
        self.play(Create(label3))
        self.wait(duration=0.25)
        self.play(Transform(title, title2))
        self.play(Transform(ax, ax2))
        self.play(Transform(graph, graph2))
        self.play(Transform(line, line4))
        self.play(Transform(label, label4))
        self.play(Transform(line2, line5))
        self.play(Transform(label2, label5))
        self.play(Transform(line3, line6))
        self.play(Transform(label3, label6))
        self.play(Create(line7))
        self.play(Create(label7))
        self.play(Create(line8))
        self.play(Create(label8))
        self.play(Create(line9))
        self.play(Create(label9))
        self.wait(duration=0.25)
        self.play(Transform(title, title3))
        self.play(Transform(ax, ax3))
        self.play(Transform(graph, graph3))
        self.play(FadeOut(line4))
        self.play(FadeOut(label4))
        self.play(FadeOut(line5))
        self.play(FadeOut(label5))
        self.play(FadeOut(line6))
        self.play(FadeOut(label6))
        self.play(FadeOut(line7))
        self.play(FadeOut(label7))
        self.play(FadeOut(line8))
        self.play(FadeOut(label8))
        self.play(FadeOut(line9))
        self.play(FadeOut(label9))
        self.play(FadeOut(line))
        self.play(FadeOut(label))
        self.play(FadeOut(line2))
        self.play(FadeOut(label2))
        self.play(Transform(line3, line10))
        self.play(Transform(label3, label10))
        self.play(Create(line11))
        self.play(Create(label11))
        self.play(FadeOut(graph))
        self.play(FadeOut(line3))
        self.play(FadeOut(label3))
        self.play(FadeOut(line11))
        self.play(FadeOut(label11))
        self.play(FadeOut(ax))
        self.play(Transform(title, message))
        self.wait()