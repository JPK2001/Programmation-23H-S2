class Heure:
    def __init__(self, heure):
        self.heure = heure
    def afficher_heure(self):
        print(f"il est: {self.heure}")
    def reinitialiser(self):
        setattr(t,"heure","0:00")
        print(f"il est maintenant: {self.heure}")

t = Heure("6:15")
t.afficher_heure()
t.reinitialiser()