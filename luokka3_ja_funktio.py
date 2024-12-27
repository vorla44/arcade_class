class Address():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""


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

#print(f"The client's main home is in {home_address.city}")
#print(f"His vacation home is in {vacation_home_address.city}")

# Tulosta osoite näytölle
def print_address(address):
    print(address.name)
    # Jos on saatavilla line1, tulosta se
    if len(address.line1) > 0:
        print(address.line1)
    # Jos löytyy line2, niin tulostetaan
    if len(address.line2) > 0:
        print( address.line2 )
        print(f"{address.city},  {address.state}  {address.zip}")

print_address(home_address)
print()
print_address(vacation_home_address)