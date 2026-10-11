# Simple Calculator
# This program performs five basic mathematical operations.

# Addition
def Add (a,b):
    return a+b

# Subtraction
def Subtract (a,b):
    return a-b

# Multiplication
def Mulitiply (a,b):
   return a*b

# Division
def Divide (a,b):
    return a/b

# Exponentiation
def Exponentiation (a,b):
    return a**b

# Calculator Loop
while True:
    print("╔════════════════════════════════╗")
    print("║           Calculator           ║")
    print("╠════════════════════════════════╣")

    print("║       1️.  ➕  Add              ║")
    print("  ══════════════════════════════")
    print("║       2️.  ➖  Subtract         ║")
    print("  ══════════════════════════════")
    print("║       3️.  ✖️   Mulitiply        ║")
    print("  ══════════════════════════════")
    print("║       4️.  ➗  Divide           ║")
    print("  ══════════════════════════════")
    print("║       5️.  🔺  Exponentiation   ║")
    print("╚════════════════════════════════╝")
    print("")

    # Get the user's choice and input numbers
    Question = float(input("🤖 : Enter the desired number :"))
    Q_number1= float(input("🤖 : Enter the first number:"))
    Q_number2= float(input("🤖 : Enter the second numbe:"))

    # Perform the selected operation
    if Question ==1:
        print( Q_number1 + Q_number2)
    elif Question ==2:
        print( Q_number1 - Q_number2)
    elif Question ==3:
        print( Q_number1 * Q_number2)
    elif Question ==4:
        print( Q_number1 / Q_number2)
    elif Question ==5:
        print( Q_number1 ** Q_number2 )
    else:
        print("")
        print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

    print("")
    # Ask whether the user wants to continue
    again=input('''🤖  :Do you want to do it again?
Y for yes and N for no''')
    if again=='Y':
        print("Ok")
    elif again=='N':
        print("see you later")
        break
    
