import customtkinter
import random

class Case():
    def __init__(self, root):
        self.root = root
        self.bomb = "💣"
        self.flag = "🚩"

    def create_button(self, x, y):
        case_button = customtkinter.CTkButton(self.root, width=35, height=35, text="", fg_color="grey", corner_radius=0)
        case_button.configure(command=lambda: self.random_button(case_button))
        case_button.place(x=x, y=y)
        return case_button

    def random_button(self, button):
        if button.cget("text") == "":
            choices = ["", "1", "2", "3", "4", "5", "6", "7", "8", self.bomb]
            choice = random.choice(choices)
            button.configure(text=choice)
