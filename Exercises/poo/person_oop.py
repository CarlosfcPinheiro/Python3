from datetime import date

class Person:
    def __init__(self, name: str, country: str, daybirht: int, monthbirth: int, yearbirth: int) -> None:
        self.name = name
        self.country = country
        self.daybirth = daybirht
        self.monthbirth = monthbirth
        self.yearbirth = yearbirth

    def calc_age(self) -> int:
        year = date.today().year
        month = date.today().month
        day = date.today().day

        age = (year - self.yearbirth) - 1
        if (month - self.monthbirth > 0):
            age += 1
        elif (month - self.monthbirth == 0):
            if (day - self.daybirth > 0):
                age += 1

        return age

def main():
    name = str(input("Enter a name: ")).strip().title()
    country = str(input("Enter a contry: ")).strip().title()
    dayb = int(input("Enter a day birth: "))
    monthb = int(input("Enter a month birth: "))
    yearb = int(input("Enter an year birth: "))

    person = Person(name, country, dayb, monthb, yearb)
    datebirht = [person.daybirth, person.monthbirth, person.yearbirth]

    print(f"""\nCredentials
    Name: {person.name}
    Country: {person.country}
    BirthDay: {datebirht[0]}/{datebirht[1]}/{datebirht[2]}
    Age: {person.calc_age()}""")

main()