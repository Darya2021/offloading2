#حذف عناصر تکراری لیست
list1 = ["ali", "reza", "tina", "darya",\
"darya", "ali", "sima", "mina", "darya"]
print(list1)
print("list length = ", len(list1))
i = 0
while i < len(list1):
    j = i + 1
    while j < len(list1):
        if list1[i] == list1[j]:
            del(list1[i])
        else:
            j = j + 1
    i = i + 1
print(list1)
print("list length = ", len(list1))