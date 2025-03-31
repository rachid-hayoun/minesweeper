import customtkinter
import case

class Plateau():
    def __init__(self, root):
        self.root = root
        self.root.configure(fg_color="black")
        self.case_instance = case.Case(self.root)
        self.frame()
        self.recursive_cases(0)

    def frame(self):
        frame = customtkinter.CTkFrame(self.root, fg_color="grey", width=600, height=60, corner_radius=0)
        frame.place(x=40, y=20)

    def case(self, x, y):
        self.case_instance.create_button(x, y)

    def recursive_cases(self, count):
        if count < 120:
            x = 40 + (count % 15) * (40 + 0.25)
            y = 90 + (count // 15) * (40 + 0.25)
            self.case(x, y)
            self.recursive_cases(count + 1)
