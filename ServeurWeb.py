from SiteWeb import *


class ServeurWeb(SiteWeb):
    def __init__(self, titre, url, typeserveur,emplacement):
        super().__init__(titre,url)
        self.typeServeur = typeserveur
        self.statutServeur = False
        self.emplacement = emplacement

    def afficherInfoServeur(self):
        print(f"Type de Serveur : {self.typeServeur}\nEmplacement : {self.emplacement}\nURL : {self.url}\nTitre : {self.titre}")
    def __repr__(self):
        return f"ServeurWeb({self.typeServeur}, {self.emplacement}, {self.url}, {self.titre})"
    def demarrerServeur(self):
        if self.statutServeur == True:
            print("Le serveur est déjà en marche...")
        else:
            self.statutServeur = True
            print("Démarrage du serveur en cours...")
    def stopperServeur(self):
        if self.statutServeur == False:
            print("Le serveur est déjà en arrêt...")
        else:
            self.statutServeur = False
            print("Arrêt du serveur en cours...")
    def afficherContenu(self):
        print("######LISTE DES CONTENUS######")
        for i in self.contenu:
            print(f">>>{i}")

city = ServeurWeb("Site web de la ville de Toronto", "www.toronto.ca","Apache","Toronto")
city.demarrerServeur()
city.ajoutContenu("Education")
city.ajoutContenu("Informatique")
city.ajoutContenu("Futurs Etudiants")
city.ajoutContenu("Campus")
city.ajoutContenu("À Propos de Nous")
city.afficherInfoServeur()
city.afficherContenu()
city.stopperServeur()