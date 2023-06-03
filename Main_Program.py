#Alexza Jean R. Catanoy
#BSCPE 1-4
#OOP Concept of Simple App Calculator with Inheritance

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mOOP Concept of Simple App Calculator".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your Programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

#Import file Test Calculator.py
from User_Interface import User_Interface
from Test_Calculator import Calculator
from Calculator_Alexza import CalculatorAlexza

ui = User_Interface()
calc = Calculator()
alexza = CalculatorAlexza()

#Constructor
def __init__(self):
    self.run()

def run(self):
    try:
        #Let the user pick among the four math operations
        math_operation = ui.input("\033[0;31m\nHi my friend! Kindly pick one math opeartion among these four (+, -, *, /): \033[1;37m")

        #Let the user type in two numbers
        num1 = ui.float(input("\033[0;33m\nKindly type in the first number you like: \033[1;37m"))
        num2 = ui.float(input("\033[0;33m\nKindly type in the second number you like: \033[1;37m"))

        #Using the math operation that the user pick, execute the calculation

        #If +, add num1 and num2 and then get the modulus
        if math_operation == "+":
            CalculatorAlexza.add()
            sum = calc.add(num1, num2)
            fmodAdd = CalculatorAlexza.fmodAdd(sum)
            CalculatorAlexza.add()
            output1 = str(sum)
            output2 = fmodAdd

        #If -, subtract num1 and num2 and then get the modulus
        elif math_operation == "-":
            diff = calc.subtract(num1, num2)
            fmodSub = CalculatorAlexza.fmodSub(diff)
            output1 = str(diff)
            output2 = fmodSub

        #If *, multiply num1 and num2 and then get the modulus
        elif math_operation == "*":
            product = calc.multiply(num1, num2)
            fmodMult = CalculatorAlexza.fmodMult(product)
            output1 = str(product)
            output2 = fmodMult

        #If /, divide num1 and num2 and then get the modulus
        elif math_operation == "/":
            qoutient = calc.divide(num1, num2)
            fmodDiv = CalculatorAlexza.fmodDiv(qoutient)
            output1 = str(qoutient)
            output2 = fmodDiv

        else:
            raise ValueError("The operation you pick is not in the option.")

        #Show the output of the program
        print("\033[0;35m\nOutput 1: \033[1;37m", output1)
        print("\033[0;35m\nOutput 2: \033[1;37m", output2)

        print("\033[0;35m~" * 90)
        #Ask the user if they want to try again for another operation and numbers
        option = input("\033[0;34m\nHi my friend! Would you like to try another operation and number? (yes/no): \033[1;37m")
            
        #If the user said yes, just repeat the whole process
        if option.lower() == "yes":
            self.run()

        #If the user said no, print "Thank you for using this simple app calculator I made." and then end program
        elif option.lower() == "no":
            print("\033[0;30m\nThank you for using this simple app calculator I made.")

        else:
            raise ValueError("The option you choose is not valid.")
   
    #Manage exceptions and apply the run method continuously
    except (ValueError) as e:
        print("Exception: ", e)
        self.run()

    except (ZeroDivisionError) as e:
        print("Exception: ")
        self.run()