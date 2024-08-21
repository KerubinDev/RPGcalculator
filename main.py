class MageOfAddition:
    def add(self, a, b):
        return a + b

class WarriorOfSubtraction:
    def subtract(self, a, b):
        return a - b

class RangerOfMultiplication:
    def multiply(self, a, b):
        return a * b

class ClericOfDivision:
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não permitida!"

# Criação dos objetos (heróis)
miguel = MageOfAddition()
vitor = WarriorOfSubtraction()
kelvin = RangerOfMultiplication()
kerubin = ClericOfDivision()

formula1 = vitor.subtract(kerubin.divide(kelvin.multiply(miguel.add(10, 5), 4), 2), 3)
print(formula1)

formula2 = vitor.subtract(kerubin.divide(miguel.add(kelvin.multiply (8, 3), 7), 5), 2)
print(formula2)

formula3 = miguel.add(kelvin.multiply(kerubin.divide(vitor.subtract(25, 5), 4), 6), 10)
print(formula3)

formula4 = vitor.subtract(kerubin.divide(kelvin.multiply(miguel.add(2, 4), 9), 3), 5)
print(formula4)
