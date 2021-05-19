import math

def usermenu():
	"Prints out the UserMenu"
	print("Choose the math operation")
	print("\n")
	print("0 - Addition")
	print("1 - Subtraction")
	print("2 - Multiplication")
	print("3 - Division")
	print("4 - Modulo")
	print("5 - Raising to a power")
	print("6 - Square root")
	print("7 - Logarithm")
	print("8 - Sine")
	print("9 - Cosine")
	print("10 - Tangent")
	print("\n\n")
	choice = input("Your option from the menu: ")
	return choice

def BackToMenu():
	bckmenu = input("Would you like to go back to user menu:(y/n) ")
	return bckmenu
	
def addition():
	"Addition of two numbers"
	first_num = input("First number: ")
	second_num = input("Second number: ")
	sum = int(first_num) + int(second_num)
	print("The sum is: ", str(sum))
	
def subtraction():
	"Subtraction of two numbers"
	first_num = input("First number: ")
	second_num = input("Second number: ")
	diff = int(first_num) - int(second_num)
	print("The difference is: ", str(diff))
	
def multiplication():
	"Multiplication of two numbers"
	first_num = input("First number: ")
	second_num = input("Second number: ")
	result = int(first_num) * int(second_num)
	print("The answer is: ", str(result))

def division():
	"Division of two numbers"
	first_num = input("First number: ")
	second_num = input("Second number: ")
	result = int(first_num) / int(second_num)
	print("The answer is: ", str(result))
	
def modulo():
	"Modulo of two numbers"
	first_num = input("First number: ")
	second_num = input("Second number: ")
	result = int(first_num) % int(second_num)
	print("The answer is: ", str(result))

def powerraise():
	"Raising to a power"
	first_num = input("Base number: ")
	second_num = input("Power number: ")
	result = int(first_num) ** int(second_num)
	print("The answer is: ", str(result))
	
def squareroot():
	"Squareroot of a number"
	first_num = input("Number: ")
	result = math.sqrt(int(first_num))
	print("The answer is: ", str(result))
	
def logarithm():
	"logarithm of a number"
	first_num = input("Numeric Value: ")
	second_num = input("Base Value: ")
	result = math.log(int(first_num), int(second_num))
	print("The answer is: ", str(result))
	
def sine():
	"Sine of a number"
	first_num = input("Number in degrees: ")
	result = math.sin(math.radians(int(first_num)))
	print("The answer is: ", str(result))
	
def cosine():
	"Cosine of a number"
	first_num = input("Number in degrees: ")
	result = math.cos(math.radians(int(first_num)))
	print("The answer is: ", str(result))

def tangent():
	"Tangent of a number"
	first_num = input("Number in degrees: ")
	result = math.tan(math.radians(int(first_num)))
	print("The answer is: ", str(result))
	
while (1):
	case = usermenu();
	if int(case) < 11:
		if int(case) == 0:
			addition()
		elif int(case) == 1:
			subtraction()
		elif int(case) == 2:
			multiplication()
		elif int(case) == 3:
			division()
		elif int(case) == 4:
			modulo()
		elif int(case) == 5:
			powerraise()
		elif int(case) == 6:
			squareroot()
		elif int(case) == 7:
			logarithm()
		elif int(case) == 8:
			sine()
		elif int(case) == 9:
			cosine()
		elif int(case) == 10:
			tangent()
		
		ans = BackToMenu();
		if (ans == "y"):
			pass
		else:
			break
		
	else:
		ans = "y"
		print("\nInvalid option!\n")
	
	
	
	
	
