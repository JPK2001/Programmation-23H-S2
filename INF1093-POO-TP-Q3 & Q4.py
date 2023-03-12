class CompteBancaire:
    def __init__(self, pin):
        self.pin = pin
        self.balance = 0
        print(f"Création de compte en cours...\nCompte créer avec succès!!! - Votre solde de départ est : {self.balance}$")
        with open (f"account_{self.pin}_transaction.txt", "w") as file:
            file.write("$$$$$$$$$$Listes des Transactions$$$$$$$$$$\n")
    def depot(self, pin_t, montant):
        self.pin_t = pin_t
        self.montant = montant
        if self.pin_t == self.pin:
            self.balance += montant
            print(f"Opération de Dépôt en cours d'exécution - Veuillez patienter...\nVous avez déposé: {self.montant}$\nVotre nouveau solde est: {self.balance}$")
            self.transaction("+Dépôt")
            return self.balance
        else:
            print("Le pin saisi est incorrect!!!")
    def retrait(self, pin_t , montant):
        self.pin_t = pin_t
        self.montant = montant
        if self.pin_t == self.pin and self.balance > self.montant:
          self.balance -= montant
          print(f"Opération de Retrait en cours d'exécution - Veuillez patienter...\nVous avez rétiré: {self.montant}$\nVotre nouveau solde est: {self.balance}$")
          self.transaction("-Retrait")
          return self.montant
        else:
            print("Erreur de pin!!! / Solde Insuffisant!!!")
    def obtenir_balance(self, pin_t):
        self.pin_t = pin_t
        if self.pin == self.pin_t:
          self.__str__()
        else:
            print("Le pin saisi est incorrect!!!")
        return self.balance
    def changer_pin(self, pin_actuel, nouveau_pin):
        self.pin_actuel = pin_actuel
        self.nouveau_pin = nouveau_pin
        if self.pin_actuel == self.pin:
            self.pin = self.nouveau_pin
            print("Votre pin a été modifié avec succès!!!")
        else:
            print("Le pin actuel saisi est incorrect - Veuillez reéssayer...")
        return self.pin
    def __repr__(self):
        return f"Votre solde actuel est: {self.balance}$"
    def __str__(self):
        print (f"Votre solde actuel est: {self.balance}$")
    def transaction(self, operation):
        self.operation = operation
        with open(f"account_{self.pin}_transaction.txt", "a") as file:
                    file.write(f"{operation} de : {self.montant}$\n")

    def affichage_transaction(self):
        with open (f"account_{self.pin}_transaction.txt", "r") as file:
            contenu_fichier = file.read()
            print(contenu_fichier)

jp = CompteBancaire(2001)