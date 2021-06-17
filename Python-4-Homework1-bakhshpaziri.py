#chape adad bakhshpazir b 2,4,6,9 dar bayn 1-100
adad = 1
while adad <= 100:
    if adad % 2 == 0 or adad % 9 == 0:
        print("in adad bahale :)")
    else:
        print(adad)
    adad += 1
