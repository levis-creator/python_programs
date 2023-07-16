number1=int(input("Number 1= "))
number2=int(input("Number 2= "))

def multiply_number(number1, number2):
    return number1*number2

result=multiply_number(number1, number2)

if result <= 1000:
    print(result)
else: 
    print("condition not met")