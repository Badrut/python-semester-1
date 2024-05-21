# maaf bu saya tidak akan ngeompol lagi x 10_000_000
#for x in range (5,0,-1):
   # print(x)

#ARRAY
#gendaan =" gatau sih wir"
#gendaans =["'dia" ," mantan "," teman "," aku '"] 
#for gendaan in gendaans:
#    print("dia suka", gendaans[0])

bintang = 5
for s in range (-1,bintang,1):
    for z in range (s):
       print(" o ", end="")
    print("")
for s in range (bintang,0,-1):
    for z in range (s):
       print(" o ", end="")
    print("")
for s in range(bintang):
    for z in range(bintang):
        if z < bintang - s - 1:
            print(" ", end="")
        else:
            print(" o ", end="")
    print("")
for s in range(bintang):
    for z in range(bintang):
        if z > s:
            print("  ", end="")
        else:
            print(" o", end="")
    print("")

