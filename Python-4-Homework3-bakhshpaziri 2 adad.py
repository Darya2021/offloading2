#bakhshpaziri 2 adad bar ham
number1=int(input("please enter a number between 2-9 \n"))
number2= 1
while number2 <= 1000:
    if number2 % number1 == 0:
        print(f"adad {number2} bar {number1} bakhshpazir ast")
    number2 += 1
