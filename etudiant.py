# tp_etudiants.py
# Commit initial : déclaration des classes Etudiant et Classe

class Etudiant:
    """
    Classe représentant un étudiant avec 3 notes et une moyenne.
    """
    def __init__(self, nom, matiere1, matiere2, matiere3):
        self.nom = nom
        self.matiere1 = matiere1
        self.matiere2 = matiere2
        self.matiere3 = matiere3
        self.moyenne = (matiere1 + matiere2 + matiere3) / 3

    def __repr__(self):
        return f"{self.nom}: M1={self.matiere1}, M2={self.matiere2}, M3={self.matiere3}, Moyenne={self.moyenne:.2f}"


class Classe:
    """
    Classe représentant une classe d'étudiants.
    """
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        """
        Ajouter un étudiant à la classe.
        """
        self.etudiants.append(etudiant)

    def trier_par_matiere1(self):
        return sorted(self.etudiants, key=lambda e: e.matiere1, reverse=True)

    def trier_par_matiere2(self):
        return sorted(self.etudiants, key=lambda e: e.matiere2, reverse=True)

    def trier_par_matiere3(self):
        return sorted(self.etudiants, key=lambda e: e.matiere3, reverse=True)

    def trier_par_moyenne(self):
        return sorted(self.etudiants, key=lambda e: e.moyenne, reverse=True)


# --- Test facultatif ---
if __name__ == "__main__":
    c = Classe()
    c.ajouter_etudiant(Etudiant("Ali", 14, 12, 16))
    c.ajouter_etudiant(Etudiant("Sara", 18, 15, 17))
    c.ajouter_etudiant(Etudiant("Yacine", 10, 11, 9))

    print("Tri par matière 1 :", c.trier_par_matiere1())
    print("Tri par matière 2 :", c.trier_par_matiere2())
    print("Tri par matière 3 :", c.trier_par_matiere3())
    print("Tri par moyenne :", c.trier_par_moyenne())