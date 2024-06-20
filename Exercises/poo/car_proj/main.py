from car import Car
from opala import Opala
from fusca import Fusca

def main():
    some_car = Car("Opala", 1990, "red", 15000, 12)
    opala = Opala("OpalaX", 1888, "azul", 20000, 15)
    fusca = Fusca("Fusca", 1881, "Branco", 80000, 24)

    print(opala.calcInst())
    print(opala.__repr__())
    print(fusca.__repr__())

    print(fusca.all)

main()