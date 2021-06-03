def mostatil(tol, arz, dastoor):

    if dastoor == "mohit":
        mohit= (tol + arz) * 2
        print("mohite mostatil = ", mohit)
    elif dastoor == "masahat":
        masahat= tol * arz
        print("masahat mostatil = ", masahat)
    else:
        print("moteasefam nemitonam mohasebe konam")


tol= int(input("tol ra vared konid\n"))
arz= int(input("arz ra vared konid\n"))
dastoor= input("mohit ya masahat?\n")
mostatil(tol, arz, dastoor)
