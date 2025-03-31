import customtkinter
from PIL import Image, ImageTk
import plateau

class Home():
    def __init__(self, root):
        self.font = ("Verdana", 21, "bold")
        self.root = root  
        self.root.configure(fg_color="black")  

        self.image = Image.open("bg.png")
        self.image = self.image.resize((700, 450), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.image)

        self.canvas = customtkinter.CTkCanvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        
        self.plateau_instance = None 
        
        self.button()

    def button(self):
        play_button = customtkinter.CTkButton(self.root, text="Jouer", fg_color="green", width=100, height=60, command=self.show_plateau,font=self.font)
        play_button.place(x=300, y=200)

    def show_plateau(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.plateau_instance = plateau.Plateau(self.root)
        
