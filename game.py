import tkinter as tk
from demineur import Demineur

def start_game(menu_window, rows, cols, mines):
    menu_window.destroy()
    game_window = tk.Tk()
    game_window.title("Démineur")
    game_window.config(bg="#2c3e50")
    Demineur(game_window, rows=rows, cols=cols, mines=mines, return_callback=lambda: show_menu())
    game_window.mainloop()

def show_level_selection():
    def set_level(level):
        if level == "Facile":
            start_game(level_window, rows=8, cols=10, mines=10)
        elif level == "Normal":
            start_game(level_window, rows=8, cols=15, mines=20)
        elif level == "Difficile":
            start_game(level_window, rows=10, cols=15, mines=30)

    level_window = tk.Tk()
    level_window.title("Sélection du niveau")
    level_window.geometry("690x440")
    level_window.config(bg="#34495e")

    title_label = tk.Label(level_window, text="Sélectionner un niveau", font=("Arial", 24, "bold"), bg="#34495e", fg="white")
    title_label.pack(pady=20)

    easy_button = tk.Button(level_window, text="Facile", font=("Arial", 18, "bold"),
                            command=lambda: set_level("Facile"),
                            bg="#2ecc71", fg="white", width=15, height=2)
    easy_button.pack(pady=10)

    normal_button = tk.Button(level_window, text="Normal", font=("Arial", 18, "bold"),
                              command=lambda: set_level("Normal"),
                              bg="#f39c12", fg="white", width=15, height=2)
    normal_button.pack(pady=10)

    hard_button = tk.Button(level_window, text="Difficile", font=("Arial", 18, "bold"),
                            command=lambda: set_level("Difficile"),
                            bg="#e74c3c", fg="white", width=15, height=2)
    hard_button.pack(pady=10)

    level_window.mainloop()