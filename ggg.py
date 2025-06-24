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

