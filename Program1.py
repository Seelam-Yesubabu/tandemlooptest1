class Calculator:
    def __init__(self,a,b,op):
        self.a=a
        self.b=b
        self.op=op

    def calculate(self):
        if self.op=="+":
            return self.a+self.b
        elif self.op=="-":
            return self.a-self.b
        elif self.op=="*":
            return self.a*self.b
        elif self.op=="/":
            return self.a/self.b
        else:
            return "Invalid operation"

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
op=input("Enter operation (+,-,*,/):")

calc = Calculator(a,b,op)
print("Result:",calc.calculate())
