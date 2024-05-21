#Diketahui jari-jari lingkaran dan luas persegi, kembalikan
#jika keliling lingkaran lebih besar dari keliling persegi dan 
#jika keliling persegi lebih besar dari keliling lingkaran.
#circle_or_square(16, 625) ➞ True
#circle_or_square(5, 100) ➞ False
#circle_or_square(8, 144) ➞ True

def circle_or_square(a,b):
    hasil= 2*3,14*a*a > 4*b
    print(hasil)
    
circle_or_square(16, 625) 
circle_or_square(5, 100) 
circle_or_square(8, 144)