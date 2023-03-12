class CompteurSimple:
    def __init__(self):
        self.compteur = 0
    def incrementer(self):
        self.compteur += 1
    def reinitialiser(self):
        self.compteur = 0
    def afficher(self):
        print(f"Compteur: {self.compteur}")
    def decrementer(self):
        self.compteur -= 1

nb = CompteurSimple()
import random
from random import *
for i in range(1,872):
    if i % 13 == 0:
        nb.incrementer()

nb.afficher()
