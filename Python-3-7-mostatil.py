def mostatil(tol, arz, dastoor):

    if dastoor == "mohit":
        mohit= (tol + arz) * 2
        return mohit
    elif dastoor == "masahat":
        masahat= tol * arz
        return masahat

tol= int(input("tol ra vared konid\n"))
arz= int(input("arz ra vared konid\n"))
dastoor= input("mohit ya masahat?\n")
result= mostatil(tol, arz, dastoor)
if dastoor == "mohit":
    print("mohit = ", result)
else:
    print("masahat = ", result)
