from Test_Calculator import Calculator
from math import fmod

class CalculatorAlexza(Calculator):
    def add(self):
        print("Override")

    def fmodAdd(self, sum):
        return fmod(sum)
    
    def fmodSub(self, diff):
        return fmod(diff)
    
    def fmodMult(self, product):
        return fmod(product)
    
    def fmodDiv(self, qoutient):
        return fmod(qoutient)