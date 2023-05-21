"""
Description of what this module does
"""
from dataclasses import dataclass
import json

@dataclass()
class Film:
    """
    Docstring. Because this is the descriptive text that appears when you hover over a function, class, module, etc.
    """
    def __init__(self, titlu,an, gen):
        self.titlu = input("Adauga titlul filmului: ")
        self.an = input(f"Anul de aparitie al filmului {self.titlu}  este: ")
        self.gen = input("Genul filmului {} este: ".format(self.titlu))
        self.salveaza_film_in_fisier()
        print(f"Filmul {self.titlu} a fost adaugat in colectia de filme.")


    # filme = {'Titlu': [], 'An aparitie': [], 'Genul Filmului': []}

    # def adauga_film(self):
    #     while True:
    #         self.titlu = input("Adauga titlul filmului: ")
    #         self.an = input(f"Anul de aparitie al filmului {self.titlu}  este: ")
    #         self.gen = input("Genul filmului {} este: ".format(self.titlu))
    #         break
    #     BibliotecaFilme.filme['Titlu'].append(self.titlu)
    #     BibliotecaFilme.filme['An aparitie'].append(self.an)
    #     BibliotecaFilme.filme['Genul Filmului'].append(self.gen)
    #     print(f"Filmul {self.titlu} a fost adaugat in colectia de filme.")

    def sterge_film(self):
      """
      se va sterge un film din colectia de filme impreuna cu toate atributele sale
      """
    pass

    def salveaza_film_in_fisier(self):
        """
        scrie in fisier cele 3 atribute
        """

        with open('colectie.json','a') as file:
            file.write(f"{{\n\ttitlu : '{self.titlu}';\n\tan : {self.an};\n\tgen : '{self.gen}'\n}}\n")
            file.close()

    def cauta_film(self, titlu):
        # sa caut filmul dupa titlu si afisez toate informatiile despre acel film
        pass
