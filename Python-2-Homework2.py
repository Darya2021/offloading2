# Tamrine2, Mohasebe shakhese BMI

weight= float(input("B narmafzare mohasebe BMI khosh amadid. \nlotfan vazne \
khod ra b kilogram vared konid: \n"))
height= float(input("lotfan ghade khod ra b metr vared konid: \n"))
BMI= weight / (height * height)

if BMI <= 18.5:
    print(f"BMI shoma {BMI} ast, shoma Laghar hastid, rejime ghazaei porkaleri \
pishnahad mishavad.")

elif 18.5 < BMI < 24.5:
    print(f"BMI shoma {BMI} ast, Ghad va vazne shoma monaseb ast.")

elif 24.5 <= BMI < 30:
    print(f"BMI shoma {BMI} ast, shoma ezafe vazn darid, varzesh va rejime \
ghazaei kamkaleri pishnahad mishavad.")

elif 30 <= BMI < 40:
    print(f"BMI shoma {BMI} ast, Moteasefane shoma chagh hastid, varzesh va \
rejime ghazaei kamkaleri pishnahad mishavad.")

else:
    print(f"BMI shoma {BMI} ast, Moteasefane shoma chaghi mofrat darid, varzesh \
va rejime ghazaei kamkaleri pishnahad mishavad.")
