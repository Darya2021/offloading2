############# Student Assistent ##########
def moraba():
    if mohit_masahat == "mohit":
        zele = int(input("zele ra vared kon \n"))
        return zele * 4
    elif mohit_masahat == "masahat":
        zele = int(input("zele ra vared kon \n"))
        return zele ** 2
    else:
        return "vorodi namotabar, dobare vared kon"
##########################################
def mostatil():
    if mohit_masahat == "mohit":
        tol = int(input("tol ra vared kon \n"))
        arz = int(input("arz ra vared kon \n"))
        return (tol + arz) * 2
    elif mohit_masahat == "masahat":
        tol = int(input("tol ra vared kon \n"))
        arz = int(input("arz ra vared kon \n"))
        return tol * arz
    else:
        return "vorodi namotabar, dobare vared kon"
#########################################
def mosalas():
    if mohit_masahat == "mohit":
        zele_1 = int(input("zele aval ra vared kon \n"))
        zele_2 = int(input("zele dovom ra vared kon \n"))
        zele_3 = int(input("zele sevom ra vared kon \n"))
        return zele_1 + zele_2 + zele_3
    elif mohit_masahat == "masahat":
        ertefa = int(input("ertefae ra vared kon \n"))
        ghaede = int(input("ghaede ra vared kon \n"))
        return (ertefa * ghaede) / 2
    else:
        return "vorodi namotabar, dobare vared kon"
#########################################
def dayere():
    if mohit_masahat == "mohit":
        shoae = int(input("shoae ra vared kon \n"))
        return (shoae * 2) * 3.14
    elif mohit_masahat == "masahat":
        shoae = int(input("shoae ra vared kon \n"))
        return shoae * shoae * 3.14
    else:
        return "vorodi namotabar, dobare vared kon"
########################################
while True:
    shekl= input("lotfan shekle moredenazar ra vared konid: m: moraba, s: mostatil,\
    l: mosalas, d: dayere\n")
    mohit_masahat= input("mohit ya masahat? \n")
    if shekl == "m":
        print("pasokhe shoma= ", moraba())
    elif shekl == "s":
        print("pasokhe shoma= ", mostatil())
    elif shekl == "l":
        print("pasokhe shoma= ", mosalas())
    elif shekl == "d":
        print("pasokhe shoma= ", dayere())
    else:
        print("vorodi namotabar, dobare vared kon")
    pasokh= input("bazam mashgh dari? are ya na \n")
    if pasokh == "are":
        continue
    else:
        print("bye")
        break
