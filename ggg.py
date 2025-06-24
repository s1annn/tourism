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
