#چاپ مجموع ارقام یک عدد ورودی
num = input("enter a number= \n")
list1= list(num)
sum1 = 0
for i in range(len(list1)):
    sum1 = sum1 + int(list1[i])
print(sum1)
