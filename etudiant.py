# tp_etudiants.py
# Commit : ajout d'un décorateur pour la 4ème matière et son itérateur

from collections.abc import Iterable

# --- Décorateur de classe pour Student et SchoolClass ---
def add_matiere4_with_iterator(default_note):
    def decorator(cls):
        # Modification du __init__ de Student pour ajouter matiere4
        if hasattr(cls, '__init__'):
            original_init = cls.__init__
            def new_init(self, *args, **kwargs):
                original_init(self, *args, **kwargs)
                self.matiere4 = default_note
            cls.__init__ = new_init
        return cls
    return decorator


@add_matiere4_with_iterator(20)  # note par défaut = 20
class Student:
    """
    Classe représentant un étudiant avec 4 matières.
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


class SchoolClass(Iterable):
    """
    Classe représentant une classe d'étudiants.
    """
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

# --- Décorateur pour ajouter l'itérateur de la 4ème matière à SchoolClass ---
def add_iterator_matiere4(cls):
    def iter_matter_4(self):
        return iter(sorted(self.students, key=lambda e: e.matiere4, reverse=True))
    cls.iter_matter_4 = iter_matter_4
    return cls

SchoolClass = add_iterator_matiere4(SchoolClass)


# --- Bloc main ---
if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('Ali', 14, 12, 16))
    school_class.add_student(Student('Sara', 18, 15, 17))
    school_class.add_student(Student('Yacine', 10, 11, 9))

    # Appel de rank matière 1
    school_class.rank_matter_1()

    # --- Test itérateur matière 4 ---
    print("\n--- Itérateur matière 4 (décorateur) ---")
    for student in school_class.iter_matter_4():
        print(f"{student.nom}: M4={student.matiere4}")