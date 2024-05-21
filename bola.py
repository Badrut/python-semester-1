
#def bola(r):
    #vol = (4/3)*(22/7)*r**3
    #print("volume bola dengan jari jari",r,"cm adalah",vol)
    #print("luas permukaan bola dengan jari jari",r,"cm adalah", luas_permukaan)
#r = int(input("masuka jari jari yang akan anda gunakan :"))
#bola(8)
#bola(10)


def kubus(rusuk):
    luas = 6*r**2
    volume = r **3

    print("luas kubus", luas)
    print("vol kubus", volume)

def balok(p, l, t):
    luas = 2*((p*1)+(p*t)+(1*t))
    volume = p*1*t
    
    print("luas balok", luas)
    print(" vol balok", volume)

def persegi(s):
    keliling = 4*s
    luas = s*s

    print('keliling persegi',keliling)
    print('luas persegi',luas)

ulang = 'ya'
while (ulang == 'ya'):
  print("perhitungan bidang ruang")
  print("silakan pilih")
  print("1. kubus")
  print("2. balok")
  print("3. persegi")
  pilihan = str(input("masukan pilihan yang anda pilih ="))
  match pilihan:
      case '1':
          r = int(input("masukan rusuk kubus ="))
          kubus(r)
      case '2':
          p =int(input("masukan panjang balok ="))
          l =int(input("masukan lebar balok ="))
          t =int(input("masukan tinggi balok ="))
          balok(p,l,t)
      case '3':
          s =int(input("masukan sisi persegi ="))
          persegi(s)
      case _ :
          print("maaf pilihan anda tidak ada")

  ulang = str(input("ulang lagi tidak? (ya/tidak)"))
