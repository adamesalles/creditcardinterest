x = float(input("Fixed Interest : "))
y = float(input("Interest per Parcels: "))
z = 0



while z < 16:
    a = (((1 + (x/100))*(1 + (y/100))**(z))-1)*100
    print("For ", z, " Parcels: ", a,"%")
    z = z + 1

