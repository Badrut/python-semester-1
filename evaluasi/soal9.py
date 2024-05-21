#Dua angka dilewatkan sebagai parameter. Parameter pertama dibagi parameter kedua akan mempunyai sisa, 
#mungkin nol. Kembalikan nilai itu. 
#remainder(1, 3) ➞ 1
#remainder(3, 4) ➞ 3
#remainder(5, 5) ➞ 0
#remainder(7, 2) ➞ 1

def remainder(a, b):
    remainder = a % b
    print(remainder)

remainder(1, 3) 
remainder(3, 4) 
remainder(5, 5) 
remainder(7, 2) 