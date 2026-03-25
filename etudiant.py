# tp_etudiants.py
# Commit : ajout d'un décorateur de classe pour la 4ème matière

from collections.abc import Iterable

# --- Décorateur pour ajouter la 4ème matière ---
def add_matiere4(default_note):
    def decorator(cls):
        original_init = cls.__init__
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.matiere4 = default_note
        cls.__init__ = new_init
        return cls
    return decorator

# --- Classe Student décorée ---
@add_matiere4(20)  # valeur par défaut de la 4ème matière = 20
class Student:
    """
    Classe représentant un étudiant avec 4 matières (la 4ème ajoutée par décorateur)
    """
    def __init__(self, nom, matiere1, matiere2, matiere3):
        self.nom = nom
        self.matiere1 = matiere1
        self.matiere2 = matiere2
        self.matiere3 = matiere3
        self.moyenne = (matiere1 + matiere2 + matiere3) / 3  # moyenne initiale sans 4ème matière

    def __repr__(self):
        return (f"{self.nom}: M1={self.matiere1}, M2={self.matiere2}, "
                f"M3={self.matiere3}, M4={self.matiere4}, Moyenne={self.moyenne:.2f}")


# --- Classe SchoolClass inchangée pour l'instant ---
class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_1(self):
        print("\n--- Classement matière 1 ---")
        for s in sorted(self.students, key=lambda e: e.matiere1, reverse=True):
            print(f"{s.nom}: {s.matiere1}")

    def __iter__(self):
        return iter(sorted(self.students, key=lambda e: e.matiere1, reverse=True))


# --- Bloc main ---
if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('Ali', 14, 12, 16))
    school_class.add_student(Student('Sara', 18, 15, 17))
    school_class.add_student(Student('Yacine', 10, 11, 9))

    # Appel méthode rank pour vérifier matière 1
    school_class.rank_matter_1()

    # --- Test de la 4ème matière ajoutée par décorateur ---
    print("\n--- Vérification de la 4ème matière ---")
    for student in school_class:
        print(f"{student.nom}: M4={student.matiere4}")