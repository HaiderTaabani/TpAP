# tp_etudiants.py

class Etudiant:
    def __init__(self, nom, matiere1, matiere2, matiere3):
        self.nom = nom
        self.matiere1 = matiere1
        self.matiere2 = matiere2
        self.matiere3 = matiere3
        self.moyenne = (matiere1 + matiere2 + matiere3) / 3

    def __repr__(self):
        return f"{self.nom}: M1={self.matiere1}, M2={self.matiere2}, M3={self.matiere3}, Moyenne={self.moyenne:.2f}"


class Classe:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    # Méthodes pour trier par matière ou moyenne (sera utilisé plus tard)
    def trier_par_matiere1(self):
        return sorted(self.etudiants, key=lambda e: e.matiere1, reverse=True)

    def trier_par_matiere2(self):
        return sorted(self.etudiants, key=lambda e: e.matiere2, reverse=True)

    def trier_par_matiere3(self):
        return sorted(self.etudiants, key=lambda e: e.matiere3, reverse=True)

    def trier_par_moyenne(self):
        return sorted(self.etudiants, key=lambda e: e.moyenne, reverse=True)