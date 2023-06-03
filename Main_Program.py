#Alexza Jean R. Catanoy
#BSCPE 1-4
#OOP Concept of Simple App Calculator with Inheritance

from User_Interface import User_Interface
from Test_Calculator import Calculator
from Calculator_Alexza import CalculatorAlexza

ui = User_Interface()
calc = Calculator()
alexza = CalculatorAlexza()

while True:
    #Pick a math operation
    math_operation = ui.user_choose()

    #Let the user type in two numbers
    num1 = ui.input_num1()
    num2 = ui.input_num2()

    #If +, add num1 and num2 and then get the modulus
    if math_operation == "+":
        alexza.add()
        sum = calc.add(num1 + num2)
        fmodAdd = alexza.fmodAdd(sum)
        alexza.add()
        output1 = str(sum)
        output2 = fmodAdd

    #If -, subtract num1 and num2 and then get the modulus
    elif math_operation == "-":
        diff = calc.subtract(num1 - num2)
        fmodSub = alexza.fmodSub(diff)
        output1 = str(diff)
        output2 = fmodSub

    #If *, multiply num1 and num2 and then get the modulus
    elif math_operation == "*":
        product = calc.multiply(num1 * num2)
        fmodMult = alexza.fmodMult(product)
        output1 = str(product)
        output2 = fmodMult

    #If /, divide num1 and num2 and then get the modulus
    elif math_operation == "/":
        qoutient = calc.divide(num1 / num2)
        fmodDiv = alexza.fmodDiv(qoutient)
        output1 = str(qoutient)
        output2 = fmodDiv

    if not ui.retry():
        
        #Show the output of the program
        print("\033[0;35m\nOutput 1: \033[1;37m", output1)
        print("\033[0;35m\nOutput 2: \033[1;37m", output2)