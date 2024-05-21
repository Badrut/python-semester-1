print("hallo world")


# A = 10 A adalah variabel yang bernilai 10

#tipe data : angka satuan yang tidak ada koma nya disebut (integer)
data_integer = 1
print(type(data_integer))
print("data :",data_integer, ", bertipe :" ,type(data_integer))

#tipe data : angka dengan koma disebut (float)
data_float= 1.5
print(type(data_float))
print("data :",data_float, ", bertipe :" ,type(data_float))

#tipe data : kumpulan karakter (string)
data_string= "ucup"
print(type(data_string))
print("data :",data_string, ", bertipe :" ,type(data_string))

#tipe data : biner true/false (boolean)
data_bool = False
print(type(data_bool))
print("data :",data_bool, ", bertipe :" ,type(data_bool))

#tipe data kusus
#bilangan kompleks
#tipe data : biner true/false (boolean)
data_complex = complex(5,6)
print(type(data_complex))
print("data :",data_complex, ", bertipe :" ,type(data_complex))

#casting
#merubah tipe data satu ke tipe data lainnya
#tipe data itu ada 4 = int,float,str,bool

print("=====INTEGER=====")
data_int = 4;
data_bool = bool(data_int)
data_str = str(data_int)
data_float = float(data_int)
print("data = ", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

print("=====boolean=====")
data_bool = 5;
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

print("=====string=====")
data_str = 10;
data_int = int(data_str )
data_bool = bool(data_str )
data_float = float(data_str )
print("data = ", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

print("=====float=====")
data_float= 10;
data_int = int(data_float )
data_bool = bool(data_float)
data_str = str(data_float )
print("data = ", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

print (" ======== BELAJAR PRINT UNTUK USER==========")
#belajar input
# data yang dimasukan pasti str
data =input ("masukan data =")
print("data = ",data,"type =", type(data))
data_int=int(input("masukan angka ="))
print("data =",data_int,"tupe =", type(data_int))
biner =bool(int(input("masukan angka biner =")))
print("Data =",biner,"type =", type(biner))

print("=============== ARITMATIK ================")
a = 10
b = 3
#tambah tambahan
hasil = a + b 
print(a,'+',b,'=',hasil)
# pengurangan
hasil = a - b
print(a,'-',b,'=',hasil)
#perkailan
hasil = a * b
print(a,'*',b,'=',hasil)
#pembangian
hasil = a / b
print(a,'/',b,'=',hasil)
#perpangkatan 
hasil = a ** b
print(a,'**',b,'=',hasil)
hasil = a // b
print(a,'//',b,'=',hasil)
hasil = a % b
print(a,'%',b,'=',hasil)

#latihan konversi satuan temperature
# program konversi celcius ke satuan lainnya 

print(" PROGRAM KONVERSI TEMPERATUR ")

celcius = float(input('masukan suhu dalam celcius :'))
print("suhu adalah",celcius,"Celcius")

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
#reamur 
reamur = (4/5)* celcius
print("suhu dalam reamur",reamur,"Reamur")

#fahrenheit
fahrenheit = ((9/5)*celcius)+ 32
print("suhu dalam fahrenheit",fahrenheit,"Fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin",kelvin,"Kelvin")

#fahrenheit to kelvin
fahrenheit = float(input("masukan suhu dalam Fahrenheit ="))
kelvin = (fahrenheit - 32)*(5/9)+273
print("Kelvin",kelvin,"K")

#kelvin to fahrenheit
kelvin = float(input("masukan suhu dalam kelvin ="))
fahrenheit = (kelvin - 273)*(5/9)+32
print("Fahrentheit",fahrenheit,"F")

print(20*'=')
print("operasi komperasi")
print(20*'=')
#setiap hasil dari komperasi adalah boolean
# >,<,<=,>=,==,!=,is , is not

a = 4
b = 2

#lebih besar dari >
hasil = a > 3
print(a,'>',3,'=',hasil)

#kurang dari <
hasil = a < 3
print(a,'<',3,'=',hasil)