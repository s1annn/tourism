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


