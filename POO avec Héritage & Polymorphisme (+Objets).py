class Employe:
    def __init__(self, id, prenom, nom):
        self.id = id
        self.prenom = prenom
        self.nom = nom
    def __str__(self):
        return f"{self.id} : {self.prenom} {self.nom}"

class EmployeTempsPlein(Employe):
    def __init__(self, id, prenom, nom, salaire_annuel):
        super().__init__(id, prenom, nom)
        self.salaire_annuel = salaire_annuel
    def calculSalaire(self):
        return self.salaire_annuel/26
    def __str__(self):
        return f"{self.id} : {self.prenom} {self.nom} | Employé à Temps Plein"

class EmployeTempsPartiel(Employe):
    def __init__(self, id, prenom, nom, nbre_heures, taux_horaires):
        super().__init__(id, prenom, nom)
        self.nbre_heures = nbre_heures
        self.taux_horaires = taux_horaires
    def calculSalaire( self ):
        return self.nbre_heures * self.taux_horaires
    def __str__(self):
        return f"{self.id} : {self.prenom} {self.nom} | Employé à Temps Partiel"

class EmployeParComission(EmployeTempsPlein):
    def __init__(self, id, prenom, nom, salaire_annuel, commission):
        super().__init__(id, prenom, nom, salaire_annuel)
        self.commission = commission
    def calculSalaire(self):
        return super().calculSalaire() + self.commission
    def __str__(self):
        return f"{self.id} : {self.prenom} {self.nom} | Employé avec Commission"

gen0 = Employe(300122, "Rayan", "Willis")
print("###Description employé###")
print(gen0.__str__())

gen1 = EmployeTempsPlein(300122, "Rayan", "Willis", 156000)
print("###Description employé###")
print(gen1.__str__())
print("+++Salaire Bi-Hebdomadaire+++")
print(f"{gen1.calculSalaire()}$")

gen2 = EmployeTempsPartiel(300122, "Rayan", "Willis", 20, 25)
print("###Description employé###")
print(gen2.__str__())
print("+++Salaire Bi-Hebdomadaire+++")
print(f"{gen2.calculSalaire()}$")

gen3 = EmployeParComission(300122, "Rayan", "Willis", 156000, 300)
print("###Description employé###")
print(gen3.__str__())
print("+++Salaire Bi-Hebdomadaire+++")
print(f"{gen3.calculSalaire()}$")