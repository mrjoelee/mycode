#!/usr/bin/env python3
"""
Joe | joe.lee@tlgcohort.com

Challenge: Conditionals Troubleshooting
"""
def main():
    """runtime"""
    # A program that prompts a user for two operators and operation (plus or minus)
    # the program then shows the result.
    # The user may enter q to exit the program.
    calc1 = 0.0
    calc2 = 0.0
    operation = ""
    while calc1 != "q":
        raw_input=input("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = raw_input.lower()
        if calc1 == "q":
            break
        calc1 = float(calc1)
        raw_input2=input("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = raw_input2.lower()
        if calc2 == "q":
            break
        calc2 = float(calc2)
        operator_input=input("Enter an operation to perform on the two operators (+ or -):")
        operation = operator_input
        if operation == "+":
            print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        elif operation == '-':
            print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        else:
            print("\n Not a valid entry. Restarting...")
if __name__=="__main__":
    main()
