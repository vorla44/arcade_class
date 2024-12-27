class Person:
    def __init__(self):
        self.name = ""
        self.Money = 0


bob = Person()
bob.name = "Bob"
bob.Money = 100

nancy = bob
nancy.name = "Nancy"
#bob.name muuttuu, koska nancy viittaa bob olioon

print(bob.name, "has", bob.Money, "dollars.")
print(nancy.name, "has", nancy.Money, "dollars.")