class ClassA():
    def __init__(self):
        self.y = 3

# Esimerkki staattisesta muuttujasta
class ClassB():
    x = 7

# Luodaan luokan instanssit
a = ClassA()
b = ClassB()

# Kaksi tapaa tulostaa staattisen muuttujan arvo
# Jälkimmäinen on se oikea tapa.
print(b.x)
print(ClassB.x)

# Yksi tapa tulostaa instanssimuuttujan arvo
# Toinen saa aikaan virheilmoituksen, koska ei ole tietoa, mihin olioon käsky kohdistuu
print(a.y)
# print(ClassA.y) virhe