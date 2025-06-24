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


class AdvantureApp:
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
