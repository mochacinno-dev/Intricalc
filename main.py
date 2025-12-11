"""
Made by The Mocha Foundation under the UNLICENSE license
on December 9th, 2025.

Project dedicated to make a calculator in the most intricate
way possible, and as bloated as possible.
"""
from bmathf import sum, dec, mul, div
from mlmathf import mod, gnd
import os

##################################
# CONSOLE CLEANING
##################################
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
##################################
# MAIN FUNCTIONALITY
##################################
def main():
    clear()
    while True:
        print("""Welcome to Intricalc, the intricate calculator.
            1. Addition
            2. Substraction
            3. Multiplication
            4. Division
            5. Modulo
            6. Ground Division
            7. Exit""")
        
        op = input(">> ")
        if op == "1":
            clear()
            v1 = int(input("N1"))
            v2 = int(input("N2"))
            
            add = sum(v1, v2)
            
            print(add)
            input("\nPRESS ANY KEY TO CONTINUE")
            clear()
            
        elif op == "2":
            clear()
            v1 = int(input("N1"))
            v2 = int(input("N2"))
            
            sub = dec(v1, v2)
            
            print(sub)
            input("\nPRESS ANY KEY TO CONTINUE")
            clear()
            
        elif op == "3":
            clear()
            v1 = int(input("N1"))
            v2 = int(input("N2"))
            
            mti = mul(v1, v2)
            
            print(mti)
            input("\nPRESS ANY KEY TO CONTINUE")
            clear()
            
        elif op == "4":
            clear()
            v1 = int(input("N1"))
            v2 = int(input("N2"))
            
            dvd = div(v1, v2)
            
            print(dvd)
            input("\nPRESS ANY KEY TO CONTINUE")
            clear()
            
        elif op == "5":
            clear()
            v1 = int(input("N1"))
            v2 = int(input("N2"))
            
            mdl = mod(v1, v2)
            
            print(mdl) 
            input("\nPRESS ANY KEY TO CONTINUE")
            clear()
            
        elif op == "6":
            clear()
            v1 = int(input("N1"))
            v2 = int(input("N2"))
            
            grn = gnd(v1, v2)
            
            print(grn)
            input("\nPRESS ANY KEY TO CONTINUE")
            clear()
            
        elif op == "7":
            clear()
            print("Thank you for using Intricalc.")
            break
        
        else:
            print("Input not valid")
            clear()
            
if __name__ == "__main__":
    main()