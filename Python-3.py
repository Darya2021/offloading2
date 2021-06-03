def BMI():
    weight= float(input("lotfan vazne khod ra b kilogram vared konid: \n"))
    height= float(input("lotfan ghade khod ra b metr vared konid: \n"))
    BMI= weight / (height * height)
    print (f"BMI shoma : {BMI}")

BMI()
