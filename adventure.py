import tkinter as tk
from tkinter import messagebox, ttk
from abc import ABC, abstractmethod

class Place(ABC):
    def __init__(self, name, cost, experience, emoji):
         self.name = name
         self.cost = cost
         self.experience = experience
         self.emoji = emoji
         self.place_type="Unknown"

    def describe(self):
      type_description = {
          "Beach": "Chill and enjoy the sun",
          "Mountain": "Enjoy beautiful views",
          "City": "Culture, shopping and exciting places"
      }
      describe = type_description.get(self.place_type.lower(), "Explore new places")
      return f"{self.emoji} {self.name} - {describe}. Cost: {self.cost}, EXP: {self.experience}"

    def interact(self, tourist):
        pass

class Beach(Place):
    def __init__(self, name, cost, experience, emoji):
            super().__init__(name, cost, experience, emoji,)
            self.place_type="Beach"

    def interact(self, tourist):
            tourist.gain_experience(self.experience)
            return f"{tourist.avatar} {tourist.name} relaxed on {self.name} beach and gained 🌞 {self.experience} EXP!"

class Mountain(Place):
    def __init__(self, name, cost, experience, emoji):
            super().__init__(name, cost, experience, emoji)
            self.place_type = "Mountain"

    def interact(self, tourist):
            gained = int(self.experience * 1.5)
            tourist.gain_experience(gained)
            return f"{tourist.avatar} {tourist.name} climbed {self.name} and gained ⭐ {gained} EXP!"

class City(Place):
    def __init__(self, name, cost, experience, emoji):
            super().__init__(name, cost, experience, emoji)
            self.place_type = "City"

    def interact(self, tourist):
            gained = int(self.experience * 0.8)
            tourist.gain_experience(gained)
            tourist.money -= 5 #random purchase

            souvenir = f"Souvenir from {self.name}"
            tourist.add_item(souvenir)
            return f"{tourist.avatar} {tourist.name} explored {self.name}, bought souvenirs and gained 🌃 {gained} EXP!"


#Player class
class Tourist:
    def __init__(self, name, money, avatar):
        self.name = name
        self.money = money
        self.experience = 0
        self.avatar = avatar
        self.level = 1
        self.inventory = []

    def gain_experience(self, amount):
        self.experience += amount
        self.level = self.experience // 100 +1


    def add_item(self, item):
            self.inventory.append(item)

    def visit(self, place: Place):
        if self.money>=place.cost:
            self.money -= place.cost
            return place.interact(self)
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
        tk.Label(self.start_frame, text="Enter your name:", font=("Arial", 12)).pack()
        self.name_entry = tk.Entry(self.start_frame, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(self.start_frame, text="Choose tour avatar:", font=("Arial", 12)).pack(pady=5)
        self.avatar_var = tk.StringVar(value=self.avatar_options[0])
        self.avatar_menu = ttk.Combobox(self.start_frame, textvariable=self.avatar_var, value=self.avatar_options, font=("Arial", 12), state="readonly")
        self.avatar_menu.pack(pady=5)

        self.start_button = tk.Button(self.start_frame, text="Start Advanture", command=self.start_game, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=10)

    def start_game(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        self.player = Tourist(name, 300, self.avatar_var.get())
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

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, bg="#4CAF50", fg="white")
        self.restart_button.pack(pady=5)


    def visit_place(self, place):
        result = self.player.visit(place)
        self.update_output(result)
        self.status_label.config(text=self.get_status())

        if self.player.money < min(p.cost for p in self.places):
            inventory = ", ".join(self.player.inventory) if self.player.inventory else "None"
            messagebox.showinfo("Game over",
                            f"You don't have enough money to continue visiting more places!\nFinal EXP: {self.player.experience}\nLevel: {self.player.level}\nInventory: {inventory}")
    def get_status(self):
        return f"{self.player.avatar} {self.player.name}'s Status | 💵 Money: {self.player.money} | ⭐ Experience: {self.player.experience} | 📈 Level: {self.player.level}"

    def update_output(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n\n")
        self.output_text.config(state='disabled')
        self.output_text.see(tk.END)

    def restart_game(self):
        self.root.destroy()
        root = tk.Tk()
        app = AdventureApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureApp(root)
    root.mainloop()

