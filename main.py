import customtkinter
from home import Home
from plateau import Plateau

root = customtkinter.CTk()
root.geometry("690x440")
root.title("Jeux de mineur")

H = Home(root)

root.mainloop()