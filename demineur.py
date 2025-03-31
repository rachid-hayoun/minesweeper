import random
import time
import tkinter as tk
from tkinter import messagebox
from case import Case

class Demineur:
    def __init__(self, master, rows=8, cols=15, mines=8, return_callback=None):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.flagged_count = 0
        self.remaining_mines = mines
        self.grid = [[Case() for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.first_click = False
        self.start_time = None
        self.timer_running = False
        self.return_callback = return_callback

        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.master, text='', width=4, height=2,
                                   command=lambda r=r, c=c: self.reveal_case(r, c),
                                   font=("Arial", 14), bg="#34495e", fg="white", relief="raised", bd=5)
                button.bind("<Button-3>", lambda event, r=r, c=c: self.toggle_flag(r, c))
                button.grid(row=r, column=c, padx=2, pady=2)
                self.buttons[r][c] = button

        self.info_frame = tk.Frame(self.master, bg="#2c3e50", bd=5, relief="ridge")
        self.info_frame.grid(row=self.rows, columnspan=self.cols, sticky='ew', pady=10)

        self.timer_label = tk.Label(self.info_frame, text='Temps: 0', font=("Arial", 14), bg="#2c3e50", fg="white")
        self.timer_label.pack(side="left", padx=20)

        self.mines_label = tk.Label(self.info_frame, text=f'Mines restantes: {self.remaining_mines}',
                                    font=("Arial", 14), bg="#2c3e50", fg="white")
        self.mines_label.pack(side="left", padx=20)

        self.flags_label = tk.Label(self.info_frame, text=f'Drapeaux: {self.flagged_count}',
                                    font=("Arial", 14), bg="#2c3e50", fg="white")
        self.flags_label.pack(side="left", padx=20)

        self.reset_button = tk.Button(self.master, text='Réinitialiser', font=("Arial", 14, "bold"),
                                      fg="white", bg="#E74C3C", command=self.reset_game, relief="raised", bd=5)
        self.reset_button.grid(row=self.rows + 1, columnspan=self.cols, sticky='ew', pady=5)

        self.return_button = tk.Button(self.master, text="Fermer", font=("Arial", 14, "bold"),
                                       fg="white", bg="#2ecc71", command=self.return_to_menu, relief="raised", bd=5)
        self.return_button.grid(row=self.rows + 2, columnspan=self.cols, sticky='ew', pady=5)

    def return_to_menu(self):
        if self.return_callback:
            self.master.destroy()
            self.return_callback()

    def place_mines(self, first_r, first_c):
        placed_mines = 0
        while placed_mines < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r != first_r or c != first_c) and not self.grid[r][c].mine:
                self.grid[r][c].mine = True
                placed_mines += 1
        self.calculate_adjacent_mines()

    def calculate_adjacent_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].mine:
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                                self.grid[r + dr][c + dc].adjacent_mines += 1

    def reveal_case(self, r, c):
        if self.game_over or self.grid[r][c].revealed:
            return

        if not self.first_click:
            self.first_click = True
            self.place_mines(r, c)
            self.start_timer()

        self.grid[r][c].revealed = True
        if self.buttons[r][c]:
            self.buttons[r][c].config(relief=tk.SUNKEN, bg="#2c3e50")

        if self.grid[r][c].mine:
            self.game_over = True
            self.show_mines()
            self.timer_running = False
            messagebox.showinfo("Perdu", "Boom! Vous avez perdu!")
            return

        if self.grid[r][c].adjacent_mines > 0:
            if self.buttons[r][c]:
                self.buttons[r][c].config(text=str(self.grid[r][c].adjacent_mines))
        else:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and not self.grid[nr][nc].revealed:
                        self.reveal_case(nr, nc)

    def toggle_flag(self, r, c):
        if self.game_over or self.grid[r][c].revealed:
            return
        case = self.grid[r][c]
        if not case.flagged and not case.questioned:
            case.flagged = True
            self.flagged_count += 1
            self.remaining_mines -= 1
            if self.buttons[r][c]:
                self.buttons[r][c].config(text='🚩', bg="#f39c12")
        elif case.flagged:
            case.flagged = False
            self.flagged_count -= 1
            self.remaining_mines += 1
            if self.buttons[r][c]:
                self.buttons[r][c].config(text='', bg="#34495e")
        self.update_labels()

    def update_labels(self):
        self.mines_label.config(text=f'Mines restantes: {self.remaining_mines}')
        self.flags_label.config(text=f'Drapeaux: {self.flagged_count}')

    def show_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].mine:
                    if self.buttons[r][c]:
                        self.buttons[r][c].config(text='💣', bg='red')

    def start_timer(self):
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f'Temps: {elapsed_time}')
            self.master.after(1000, self.update_timer)

    def reset_game(self):
        self.__init__(self.master, self.rows, self.cols, self.mines, self.return_callback)