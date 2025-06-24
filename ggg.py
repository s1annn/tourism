import tkinter as tk
from tkinter import messagebox, ttk
from abc import ABC, abstractmethod

class Place(ABC):
    def __init__(self, name, cost, experience, emoji):
         self.name = name
         self.cost = cost
         self.experience = experience
         self.emoji = emoji

    def describe(self):
      pass
#Classes for different places
class Beach(Place):
    def describe(self):
        return f"{self.emoji} {self.name}' - Chill and enjoy the sun. Cost : {self.cost}, EXP : {self.experience}"

class Mountain(Place):
    def describe(self):
        return f"{self.emoji} {self.name}' - Enjoy beautiful views! Cost : {self.cost}, EXP: {self.experience}"

class City(Place):
    def describe(self):
         return f"{self.emoji} {self.name}' - Culture, shopping and exiting places. Cost: {self.cost}, EXP : {self.experience}"

#Player class
class Tourist:
    def __init__(self, name, money, avatar):
        self.name = name
        self.money = money
        self.experience = 0
        self.avatar = avatar

    def visit(self, place:Place):
        if self.money >= place.cost:
            self.money -= place.cost
            self.experience += place.experience
            return f"{self.avatar} {self.name} visited {place.name}\nGained ⭐ {place.experience} EXP | 💵 Money left: {self.money}"
        else:
            return f"Not enough money to visit {place.name}."


class AdventureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventures")

        self.places = [
            Beach("Maldives", 20 ,5, "🏝️"),
            Mountain("Himalayas", 30,10, "⛰️"),
            City("Milan",15,7.5, "🌃" ),
            Beach("Bali", 10, 5, "🍹"),
            Mountain("Everest", 50, 25, "🗻"),
            City("Paris", 20, 10, "🗼"),
            Beach("Punta Cana", 40,  20, "🌊"),
            Mountain("Alps", 35, 17.5, "🏞️"),
            City("Tokyo", 60, 30, "⛩️"),
        ]

        self.avatar_options = ["🧔🏻","👩","👥️","👨🏻‍💻","🤑"]
        self.create_start_screen()

    def create_start_screen(self):
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack()

        tk.Label(self.start_frame, text="Welcome to Advantures! Choose your avatar:", font=("Arial", 14)).pack(pady=10)

        self.avatar_var = tk.StringVar(value=self.avatar_options[0])
        self.avatar_menu = ttk.Combobox(self.start_frame, textvariable=self.avatar_var, values=self.avatar_options, font=("Arial", 12), state="readonly")
        self.avatar_menu.pack(pady=5)

        self.start_button = tk.Button(self.start_frame, text="Start Advanture", command=self.start_game, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=10)
    def start_game(self):
        self.player = Tourist("Marek", 300, self.avatar_var.get())
        self.start_frame.destroy()
        self.create_game_widgets()

    def create_game_widgets(self):
        self.status_label = tk.Label(self.root, text=self.get_status(), font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        for place in self.places:
            btn = tk.Button(self.buttons_frame, text=place.describe(), width=60, command=lambda p=place: self.visit_place(p))
            btn.pack(pady=2)

        self.output_text = tk.Text(self.root, height=10, width=70, state="disabled", wrap="word")
        self.output_text.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=5)


    def visit_place(self, place):
        result = self.player.visit(place)
        self.update_output(result)
        self.status_label.config(text=self.get_status())

        if self.player.money < min(p.cost for p in self.places):
            messagebox.showinfo("Game over",
                            f"You don't have enough money to continue visiting more places!\nFinal EXP: {self.player.experience}")
            self.root.destroy()

    def get_status(self):
        return f"{self.player.avatar} {self.player.name}'s Status | 💵 Money: {self.player.money} | ⭐ Experience: {self.player.experience}"

    def update_output(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n\n")
        self.output_text.config(state='disabled')
        self.output_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureApp(root)
    root.mainloop()

