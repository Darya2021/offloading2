# Tamrine mashin hesab, 2 adad vorodi ra gerefte va amale riazi ra anjam dahad.

number_1= float(input("B narmafzare mashinhesab khosh amadid. \nlotfan adade \
aval ra vared konid: \n"))
number_2= float(input("lotfan adade dovom ra vared konid: \n"))
operator= input("lotfan amalgare riazi ra vared konid: \n+ jame, - tafrigh, \
* zarb, / taghsim, ** tavan  \n")

if operator == "+":
    print(f"Hasele {number_1} {operator} {number_2} = ", number_1 + number_2)

elif operator == "-":
    print(f"Hasele {number_1} {operator} {number_2} = ", number_1 - number_2)

elif operator == "*":
    print(f"Hasele {number_1} {operator} {number_2} = ", number_1 * number_2)

elif operator == "/":
    if number_2 == 0:
        print("adad bar 0 ghable taghsim nist")
    else:
        print(f"Hasele {number_1} {operator} {number_2} = ", number_1 / number_2)

elif operator == "**":
    print(f"Hasele {number_1} {operator} {number_2} = ", number_1 ** number_2)

else:
    print("Moteasefane pasokhi nadaram.")
