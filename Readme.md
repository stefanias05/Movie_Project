Proiect 

Clasa trebuie să conțină mai multe metode, inclusiv una pentru salvarea informațiilor despre filme într-un fișier.

## Cerințe
1. clasa BibliotecaDeFilme cu următoarele metode:

- `adauga_film(self, titlu, an, gen)`: Această metodă va adăuga un film în colecție.
- `sterge_film(self, titlu)`: Această metodă va șterge un film din colecție în funcție de titlul său.
- `cauta_film(self, titlu)`: Această metodă va căuta un film în colecție după titlu și va returna informațiile despre film dacă este găsit.
- `filme_dupa_gen(self, gen)`: Această metodă va returna o listă cu toate filmele din colecție care aparțin unui anumit gen.
- `salveaza_filme_in_fisier(self)`: Această metodă va salva informațiile despre filmele din colecție într-un fișier.
- `modifica_film(self, titlu, an_nou=None, gen_nou=None)`: Această metodă va modifica informațiile despre un film existent în colecție.
- `filme_dupa_an(self, an)`: Această metodă va returna o listă cu toate filmele din colecție care au fost lansate într-un anumit an.
- `numara_filme(self)`: Această metodă va returna numărul total de filme din colecție.
- `importa_filme_din_fisier(self)`: Această metodă va citi informațiile despre filme dintr-un fișier și le va adăuga în colecție.
- `top_filme(self, numar_filme, gen=None)`: Această metodă va returna o listă cu primele `numar_filme` filme din 
colecție, sortate descrescător după anul lansării.

2. Creare teste pentru clasa `BibliotecaDeFilme` și pentru metodele sale.  Testare scenarii precum
adăugarea, ștergerea și căutarea filmelor, precum și salvarea informațiilor despre filme într-un fișier.

3. gestionarea excepțiilor în metodele `salveaza_filme_in_fisier` și `importa_filme_din_fisier` pentru a
vă asigura că programul dvs. gestionează în mod corespunzător cazurile în care fișierul nu poate fi citit, scris sau nu există.

4. funcționalitate care să permită utilizatorului să interacționeze cu clasa BibliotecaDeFilme printr-o interfață în linia de comandă.
Utilizatorul trebuie să poată alege și să execute oricare dintre metodele disponibile prin introducerea unor comenzi simple în consolă. 
Asigurați-vă că informațiile introduse de utilizator sunt validate înainte de a fi procesate.


# PostegreSQL
# Text wrap



```markdown
1. Adauga film
2. Sterge film
3. Cauta film
4. Filme dupa gen
5. Filme dupa an
6. Salveaza filme in fisier
7. Importa filme din fisier
8. Top filme
9. Iesi din program

Alege o optiune:
```

