# tp_etudiants.py
# Commit : ajout des méthodes rank_matter_2 et rank_matter_3

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


class SchoolClass:
    """
    Classe représentant une classe d'étudiants.
    """
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # Méthodes de tri
    def trier_par_matiere1(self):
        return sorted(self.students, key=lambda e: e.matiere1, reverse=True)

    def trier_par_matiere2(self):
        return sorted(self.students, key=lambda e: e.matiere2, reverse=True)

    def trier_par_matiere3(self):
        return sorted(self.students, key=lambda e: e.matiere3, reverse=True)

    def trier_par_moyenne(self):
        return sorted(self.students, key=lambda e: e.moyenne, reverse=True)

    # --- Méthodes rank pour chaque matière ---
    def rank_matter_1(self):
        print("\n--- Classement par matière 1 ---")
        for e in self.trier_par_matiere1():
            print(f"{e.nom}: {e.matiere1}")

    def rank_matter_2(self):
        print("\n--- Classement par matière 2 ---")
        for e in self.trier_par_matiere2():
            print(f"{e.nom}: {e.matiere2}")

    def rank_matter_3(self):
        print("\n--- Classement par matière 3 ---")
        for e in self.trier_par_matiere3():
            print(f"{e.nom}: {e.matiere3}")


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