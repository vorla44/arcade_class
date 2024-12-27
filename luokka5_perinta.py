class Person():
    def __init__(self):
        self.name = ""

    def report(self):
        # perusraportti
        print("Report for", self.name)

class Employee(Person):
    def __init__(self):
        # kutsuu yliluokan (parent/super class) konstruktoria ensin
        super().__init__()

        # asetetaan muuttuja
        self.job_title = ""

    def report(self):
        # tässä määritellään uudelleen report ja suoritetaan vain tämä:
        print("Employee report for", self.name)

class Customer(Person):
    def __init__(self):
        super().__init__()
        self.email = ""

    def report(self):
        # suoritetaan yliluokan report:
        super().report()
        # Lisätään vielä oma juttu loppuun ja suoritetaan molemmat
        print("Customer e-mail:", self.email)

john_smith = Person()
john_smith.name = "John Smith"

jane_employee = Employee()
jane_employee.name = "Jane Employee"
jane_employee.job_title = "Web Developer"

bob_customer = Customer()
bob_customer.name = "Bob Customer"
bob_customer.email = "send_me@spam.com"

john_smith.report()
jane_employee.report()
bob_customer.report()