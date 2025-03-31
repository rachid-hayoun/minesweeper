import tkinter as tk
from game import show_level_selection

def show_menu():
    def go_to_level_selection():
        menu_window.destroy()
        show_level_selection()

    menu_window = tk.Tk()
    menu_window.title("Menu principal")
    menu_window.geometry("690x440")
    menu_window.config(bg="#34495e")

    title_label = tk.Label(menu_window, text="Bienvenue dans le Démineur", font=("Arial", 24, "bold"), bg="#34495e", fg="white")
    title_label.pack(pady=20)

    play_button = tk.Button(menu_window, text="Jouer", font=("Arial", 18, "bold"),
                            command=go_to_level_selection,
                            bg="#3498db", fg="white", width=15, height=2)
    play_button.pack(pady=40)

    menu_window.mainloop()