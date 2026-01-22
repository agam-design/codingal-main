class calculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "cannot divide by zero"
        else:
            return "invalid operator"
        
    def display(self):
        result = self.calculate()
        print("result:", result)


num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operator = input("enter operator(+,-,*,/): ")

calc = calculator(num1, num2, operator)
calc.display()
