#while
adad = 0
while adad <= 100:
    print(adad)
    soal=input("beram bala ya paeen ya base? \n")
    if soal == "bala":
        adad +=1
    elif soal == "paeen":
        adad -= 1
    else:
        break

print("bye")
