def tambah(x,y):
    return x + y
def kurang(x,y):
    return x - y
def kali(x,y):
   return x * y
def bagi(x,y):
    if y != 0:
     return x/y
    else:
       print("tidak dapat membagi dengan angka nol")

while True:
   print("Pilih operasi:")
   print("1. Penjumlahan")
   print("2. Pengurangan")
   print("3. Perkalian")
   print("4. Pembagian")
   print("5. Keluar")
   pilihan = str(input("masukan pilihanmu ="))
   if 5 :
      print("terimaksih suadah memakai calculator")
      break
   
   num1 = float(input("masukan angka pertama ="))
   num2 = float(input("masuka angka kedua ="))

   match pilihan:
      case '1':
         print("hasil =",tambah(num1,num2))
      case '2':
         print("hasil =",kurang(num1,num2))
      case '3':
         print("hasil =",kali(num1,num2))
      case '4':
         print("hasil =",bagi(num1,num2))
      case _:
         print("pilihan yang anda cari tidak di temukan ")


         
