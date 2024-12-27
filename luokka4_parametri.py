class Dog():
 # Konstruktori jossa parametri
    def __init__(self, new_name):
        self.name = new_name
        print(f"{self.name} niminen koira on luotu")
# Tässä luodaan koiraolio
my_dog = Dog("Spot")