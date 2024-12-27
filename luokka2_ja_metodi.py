class Address():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def print_address(self):
        print(self.name)
        # Jos on saatavilla line1, tulosta se
        if len(self.line1) > 0:
            print(self.line1)
        # Jos löytyy line2, niin tulostetaan
        if len(self.line2) > 0:
            print(self.line2)
            print(f"{self.city},  {self.state}  {self.zip}")

# Luodaan address-olio
home_address = Address()

# Asetetaan olion kenttien arvot
home_address.name = "John Smith"
home_address.line1 = "701 N. C Street"
home_address.line2 = "Carver Science Building"
home_address.city = "Indianola"
home_address.state = "IA"
home_address.zip = "50125"

# Luodaan toinen olio
vacation_home_address = Address()

# Asetetaan tämän toisen olion kenttien arvot
vacation_home_address.name = "John Smith"
vacation_home_address.line1 = "1122 Main Street"
vacation_home_address.line2 = ""
vacation_home_address.city = "Panama City Beach"
vacation_home_address.state = "FL"
vacation_home_address.zip = "32407"

home_address.print_address()
print()
vacation_home_address.print_address()