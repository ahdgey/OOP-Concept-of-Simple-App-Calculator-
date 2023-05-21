#Alexza Jean R. Catanoy
#BSCPE 1-4
#OOP Concept of Simple App Calculator

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mOOP Concept of Simple App Calculator".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your Programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

class Calculator:

    #Constructor
    def __init__(self):
        self.run()

    def run(self):
        try:
            #Let the user pick among the four math operations
            math_operation = input("Hi my friend! Kindly pick one math opeartion among these four (+, -, *, /)")

    #Let the user type in two numbers
    #Using the math operation that the user pick, execute the calculation
    #Execute the calculation
    #Show the output of the program
    #Ask the user if they want to try again for another operation and numbers
    #If the user said yes, just repeat the whole process
    #If the user said no, print "Thank you for using this simple app calculator I made." and then end program
    #Manage exceptions and apply the run method continuously