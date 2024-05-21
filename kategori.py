bb = int(input("masukan berat dalam bentuk KG : "))
tb= int(input("masukan tinggi dalam bentuk M : "))
bmi =bb/((tb/100)**2)

if( bmi <18.5):
    print("berat badan kurang opsional")
elif( bmi >=18.5 and bmi <23):
    print(" berat badan ideal ")
elif( bmi >=23 and bmi <30):
    print("berat badan berlebih")
else:
    print("obesitas")
