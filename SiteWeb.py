class SiteWeb:
    def __init__(self, titre, url):
        self.titre = titre
        self.url = url
        self.contenu = []
    def afficherTitre(self):
        return self.titre
    def afficherUrl(self):
        return self.url
    def ajoutContenu(self, c):
        self.contenu.append(c)
    def __repr__(self):
        return f"SiteWeb({self.titre}, {self.url})"
boreal = SiteWeb("Site du Collège Boréal","www.collegeboreal.ca")
boreal.ajoutContenu("Education")
boreal.ajoutContenu("Informatique")
boreal.ajoutContenu("Futurs Etudiants")
boreal.ajoutContenu("Campus")
boreal.ajoutContenu("À Propos de Nous")
