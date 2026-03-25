# tp_etudiants.py
# Commit 2 : ajout de la méthode rank_matter_1

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
        self.etudiants.append(etudiant)

    # Méthodes déjà existantes
    def trier_par_matiere1(self):
        return sorted(self.etudiants, key=lambda e: e.matiere1, reverse=True)

    def trier_par_matiere2(self):
        return sorted(self.etudiants, key=lambda e: e.matiere2, reverse=True)

    def trier_par_matiere3(self):
        return sorted(self.etudiants, key=lambda e: e.matiere3, reverse=True)

    def trier_par_moyenne(self):
        return sorted(self.etudiants, key=lambda e: e.moyenne, reverse=True)

    # --- Nouvelle méthode pour le 2ème commit ---
    def rank_matter_1(self):
        """
        Affiche les étudiants triés par matière 1 (ordre décroissant).
        """
        print("\n--- Classement par matière 1 ---")
        for e in self.trier_par_matiere1():
            print(f"{e.nom}: {e.matiere1}")


# --- Bloc main ---
if __name__ == "__main__":
    c = Classe()
    c.ajouter_etudiant(Etudiant("Ali", 14, 12, 16))
    c.ajouter_etudiant(Etudiant("Sara", 18, 15, 17))
    c.ajouter_etudiant(Etudiant("Yacine", 10, 11, 9))

    # Appel de la méthode rank_matter_1
    c.rank_matter_1()