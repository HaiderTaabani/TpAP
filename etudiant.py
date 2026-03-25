# tp_etudiants.py
# Commit 3 : SchoolClass devient Iterable avec itérateur pour matière 1

from collections.abc import Iterable, Iterator

class Student:
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


class SchoolClass(Iterable):
    """
    Classe représentant une classe d'étudiants et iterable pour matière 1.
    """
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def trier_par_matiere1(self):
        return sorted(self.students, key=lambda e: e.matiere1, reverse=True)

    # --- Méthodes rank ---
    def rank_matter_1(self):
        print("\n--- Classement par matière 1 ---")
        for e in self.trier_par_matiere1():
            print(f"{e.nom}: {e.matiere1}")

    def rank_matter_2(self):
        print("\n--- Classement par matière 2 ---")
        for e in sorted(self.students, key=lambda e: e.matiere2, reverse=True):
            print(f"{e.nom}: {e.matiere2}")

    def rank_matter_3(self):
        print("\n--- Classement par matière 3 ---")
        for e in sorted(self.students, key=lambda e: e.matiere3, reverse=True):
            print(f"{e.nom}: {e.matiere3}")

    # --- Méthode pour Iterable ---
    def __iter__(self):
        """
        Renvoie un itérateur qui parcourt les étudiants du meilleur au pire en matière 1.
        """
        return iter(self.trier_par_matiere1())


# --- Bloc main ---
if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('Ali', 14, 12, 16))
    school_class.add_student(Student('Sara', 18, 15, 17))
    school_class.add_student(Student('Yacine', 10, 11, 9))

    # Appels des méthodes rank
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    # --- Test de l'itérable ---
    print("\n--- Parcours des étudiants avec __iter__ (matière 1) ---")
    for student in school_class:
        print(f"{student.nom}: {student.matiere1}")