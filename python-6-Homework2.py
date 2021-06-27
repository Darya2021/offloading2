#مجموع مقادیر آیتم های لیست با تابع بازگشتی
def sum_list(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return sum_list(list1[1:]) + list1[0]
        
list1= [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("list is = ", list1)
print("sum values of list's items= ", sum_list(list1))
