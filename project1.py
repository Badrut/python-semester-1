def PerubahanEnergiPanas(m,c,dT): #7
    q = m*c*dT
    print(q)

def TeoremaPythagoras(a,b): #17
    c= (a**2)+(b**2)
    print(c)

def hambatan_total_seri(hambatan_seri): #3
    hambatan= 0 
    for h in hambatan_seri:
        hambatan += h
    return hambatan
        
def hambatan_total_paralel(hambatan):
    total_hambatan = 0
    for h in hambatan:
        total_hambatan += 1 / h
    total_hambatan = 1 / total_hambatan
    return total_hambatan
    
def energipotensial(m,g,h): #9
    hasil = m*g*h
    print(hasil)
    
def energimekanik(ek,em):
    hasil = ek+em
    print(hasil)
    
def PersamaanLinier1Variabel(a,b): #2
    if a == 0:
        if b == 0:
            return "persamaan ini memiliki banyak solusi"
        else :
            return "tidak memiliki solusi"
    
    else :
        x=-b/a
        return x
        

def PersamaanLinear2Variabel(a1,b1,c1,a2,b2,c2): #20
    detA = a1 * b2 - a2 * b1

    if detA  != 0:
        x = (c1 * b2 - c2 * b1) / detA
        y = (a1 * c2 - a2 * c1) / detA
        return x, y
    else:
        return None


       
def Tekanan(p,q,h): #8
    tekanan = p*q*h
    print(tekanan)
def gayaapung(p,v,q):
    gayaapung= p*v*q
    print(gayaapung)

def mean(angka):
    total = 0
    jumlah_angka = 0

    for angka_item in angka:
        total += angka_item
        jumlah_angka += 1
    
    if jumlah_angka >0:

        rata_rata = total/ jumlah_angka
        return rata_rata

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        median = sorted_data[n // 2]
    
    else:
        middle1 = sorted_data[(n // 2) - 1]
        middle2 = sorted_data[n // 2]
        median = (middle1 + middle2) / 2.0
    
    return median
def gayacoulumb(q1,q2,r):
    K = 9000000000
    F =((K*q1*q2)/r)
    print(F)
#
def kategorigempa(magnitude):
    if magnitude <5 :
        print("tidak ada gempa ")

    elif magnitude <=20 and magnitude <50:  
        print("gempe micro")
    elif magnitude >=50 and magnitude <100 :
        print("gempa minor")
    elif magnitude <100 :
        print("gempa ringan") 

    else:
        print("gempa super besar")
#6
def energikinetik(m,deltav):
    hasil = 0.5*m*(deltav**2)
    print(hasil)
#10
def gaya(m,a):
    gaya = m*a
    print(gaya)

def usaha(f,s):
    usaha = f*s
    print(usaha)
#11
def masajenis(m,v):
    hasil = m/v
    print(hasil)

def kecepatan(s,t):
    hasil = s/t
    print(hasil)
#12
def daya(w,t):
    hasil = w/t
    print(hasil)

def energikinetic(m,v):
    hasil = 0.5*m*(v**2)
    print(hasil)
#13
def  cepatrambut(lamda,t):
    v = lamda/t
    print(v)
def tekanan(f,a):
    p = f/a
    print(p)
#14
def celcius(f):
    celsius = (f - 32) * 5/9
    print(celsius)
    
#15
def percepatan(deltav, deltat):
    a = deltav/deltat
    print(a)
#16
def energipotensialgravitasi(m,g,deltah):
    w = m*g*deltah
    print(w)

def bola1(r):
    v  = (4/3)*(3.14)*r**3
    l = 4*(3.14)*r**2
    print(v)
    print(l)
    
def bola2(r):
    v  = (4/3)*(22/7)*r**3
    l = 4*(22/7)*r**2
    print("volume adlaah",v)
    print("luas adlaah",l)

def kerucut1(r,h):
    pi = 3.14
    v = (1/3)*pi*r**2*h
    lp = pi*r*(r+s)
    la = pi*r**2

    print("volume kerucut adalah",v)
    print("luas permukaan kerucut adalah",lp)
    print("luas alas kerucut adalah",la)

def kerucut2(r,h,s):
    pi = 22/7
    v = (1/3)*pi*r**2*h
    lp = pi*r*(r+s)
    la = pi*r**2

    print("volume kerucut adalah",v)
    print("luas permukaan kerucut adalah",lp)
    print("luas alas kerucut adalah",la)

def Perisma_Segitiga_Sama_Sisi(a,p,t):
    l = 2*a*p*t
    v = (1/4)*a*t
    print(l)
    print(v)

def Prisma_Segitiga_Sembarang(a,p,t):
    l = a+p+t
    v = (1/2)*a*t
    print(l)
    print(v)
    
def kategorisegitiga(sudut):
    if sudut > 90 and sudut <=180:
        print("sudut tumpul")
    elif sudut == 90:
        print("sudut siku siku")
    elif sudut < 90:
        print("sudut lancip")
    else:
        print("tidak berbentuk segitiga ")
    
def bilangan_ganjil(daftar):
    bilangan_ganjil = []
    for angka in daftar:
        if angka %2 != 0:
            bilangan_ganjil.append(angka)
    return bilangan_ganjil

    




ulang = 'ya'
while (ulang == 'ya'):

    print(10*'=')
    print("Pilih operasi:")
    print("1. Perubahan energi panas")
    print("2. Mencari c")
    print("3. Rangkaian resistor parallel dan seri")
    print("4. Energi Potensial dan Energi mekanik")
    print("5. Persamaan linier 1 variabel")
    print("6. Membuktikan kebenaran dari persamaan 2 variable")
    print("7. Tekanan dan Gaya apung")
    print("8.  (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("9.  (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("10. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("11. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("12. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("13. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("14. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("15. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("16. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("17. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("18. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("19. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("20. (COOMING SOON) pembuat codingan sedang mencari bodrex")
    print("21. (COOMING SOON) pembuat codingan sedang mencari bodrex")


    
    pilihan = str(input("masukan pilihan yang anda pilih ="))
    match pilihan:
        case '1':
            m = float(input("masukan massa  ="))
            c = float(input("masukan celcius ="))
            dT= float(input("masukan perubahan suhu benda ="))
            PerubahanEnergiPanas(m,c,dT)
        case '2':
            a = float(input("masukan angka a ="))
            b = float(input("masukan angka b ="))
            TeoremaPythagoras(a,b)
        case '3':
            while True:
                print("1. Rangkaian Seri")
                print("2. Rangkaian Parallel")
                print("3. keluar")

                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    n = int(input("masukan berapa rangkaian yang anda butuhkan ="))
                    hambatan_seri = []

                    for i in range(n):
                        h = float(input(f"masukan nilai ke-{i + 1} ohm ="))
                        hambatan_seri.append(h)
                    
                    total_hambatan_seri = hambatan_total_seri(hambatan_seri)
                    
                    print("Hambatan total dalam rangkaian seri adalah {:.2f} ohm".format(total_hambatan_seri))
    

                elif pilihan == '2':
                    n = int(input("masukan berapa rangkain yang anda butuhkan =")) 
                    hambatan_parallel = []

                    for i in range(n):
                        h = float(input(f"masukan nilai ke-{i+1}ohm ="))
                        hambatan_parallel.append(h)

                    total_hambatan_parallel = hambatan_total_paralel(hambatan_parallel)
                    print("hambatan total dalam rangkaian parallel {:.2f}ohm".format(total_hambatan_parallel))
                    
                else:
                    print("trimakasih")
                    break
                    
        case '4' :
            while True:
                print("1. Usaha Energi")
                print("2. Pesawat Sederhana")
                print("3. Keluar")

                pilihan = str(input("masukan pilihan anda (1/2/3) ="))

                if pilihan == '1':
                    m = float(input("masukan nilai massa ="))
                    g = float(input('masukan nilai gravitasi ='))
                    h = float(input("masukan nilai ketinggian ="))
                    energipotensial(m,g,h)
                
                elif pilihan == '2':
                    ek = float(input("masukan nilai energi kinetik ="))
                    em = float(input('masukan nilai energi mekanik ='))        
                    energimekanik(ek,em)
                
                else:
                    print("trimakasih")
                    break
        
        case '5':
            a = int(input("masukan nilai a ="))
            b = int(input("masukan nilai b ="))
            solusi = PersamaanLinier1Variabel(a,b)

            if isinstance(solusi ,str):
                print(f"hasil : {solusi}")
            else:
                print(f"hasil x : {solusi}")
        
        case '6':
            print("terdapat 6 variabel yang anda dapat isikan ")
            a1 = float(input("masukan nilai pertama = "))
            b1 = float(input("masukan nilai kedua = "))
            c1 = float(input("masukan nilai ketiga = "))
            a2 = float(input("masukan nilai keempat = "))
            b2 = float(input("masukan nilai kelima ="))
            c2 = float(input("masukan nilai keenam ="))
            
            solusi = PersamaanLinear2Variabel(a1,b1,c1,a2,b2,c2)

            if solusi:
                x, y =solusi
                print(f"nilai x= {x} nilai y={y}")
            
            else:
                print("persaman variable tidak ditemukan")
                break
        case '7':
            while True:
                print("1. tekanan")
                print("2. gaya apung")
                print("3. keluar")

                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    p = float(input("masukan nilai massa ="))
                    q = float(input('masukan nilai gravitasi ='))
                    h = float(input("masukan nilai ketinggian ="))
                    Tekanan(p,q,h)
                elif pilihan == '2':
                    p = float(input("masukan nilai massa ="))
                    v = float(input('masukan nilai gravitasi ='))
                    q = float(input("masukan nilai ketinggian ="))
                    gayaapung(p,v,q)
        
                else:
                    print("trimakasih")
                    break
                
        case '8':
            while True:
                print("1. Mean")
                print("2. Median")
                print("3. Keluar")
                
                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                        input_angka = input("Masukkan angka-angka (pisahkan dengan spasi): ")
                        angka = (float(x)for x in input_angka.split())
                        hasil = mean(angka)
                        
                        if hasil is not None:
                            print("Nilai rata-rata adalah:", hasil)
                        
                        else:
                            print("Daftar angka kosong. Tidak dapat menghitung rata-rata.")

                elif pilihan == '2':
                    try:
                        input_data = input("Masukkan angka-angka yang ingin dihitung median (pisahkan dengan spasi): ")
                        data = (float(x)for x in input_data.split())
                        median = median(data)
                        print("median :",median)
                    
                    except ValueError:
                        print("Masukkan yang Anda berikan tidak valid. Pastikan memasukkan angka yang valid.")
                else:
                    print("trimakasih")
                    break

        case '9':
            q1 = float(input("masukan nilai q1 ="))
            q2 = float(input("masukan nilai q2 ="))
            r = float(input("masukan nilai r ="))
            gayacoulumb(q1,q2,r)
        
        case '10':
            magnitudo = float(input("masukan ="))
            kategori = kategorigempa(magnitudo)
        
        case '11':
            m = float(input("Masukkan massa : "))
            deltav = float(input("Masukkan deltav : "))
            kinetik =energikinetik(m,deltav)
        
        case '12':
            while True:
                print("1. Gaya")
                print("2. Usaha")
                print("3. Keluar")
                
                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    m = float(input("masukan nilai massa ="))
                    a = float(input('masukan nilai gravitasi ='))
                    gaya(m,a)
                elif pilihan == '2':
                    f = float(input("masukan nilai massa ="))
                    s = float(input('masukan nilai gravitasi ='))
                    usaha(f,s)
                else:
                    print("trimakasih")
                    break
            
        case '13':
            while True:
                print("1. Gaya")
                print("2. Usaha")
                print("3. Keluar")
                
                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    m = float(input("masukan jarak ="))
                    v = float(input('masukan waktu tempuh ='))
                    masajenis(m,v)
                elif pilihan == '2':
                    w = float(input("masukan energi listrik  ="))
                    t = float(input('masukan waktu ='))
                    daya(w,t)
                else:
                    print("trimakasih")
                    break
            
        case '14':
            while True:
                print("1. Gaya")
                print("2. Usaha")
                print("3. Keluar")
                
                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    m = float(input("masukan jarak ="))
                    t = float(input('masukan waktu tempuh ='))
                    daya(w,t)
                elif pilihan == '2':
                    m = float(input("masukan energi listrik  ="))
                    v = float(input('masukan waktu ='))
                    energikinetic(m,v)
                else:
                    print("trimakasih")
                    break
        
        case '15':
            while True:
                print("1. Gaya")
                print("2. Usaha")
                print("3. Keluar")
                
                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    lamda = float(input("masukan jarak ="))
                    t = float(input('masukan waktu tempuh ='))
                    cepatrambut(lamda,t)
                elif pilihan == '2':
                    f = float(input("masukan energi listrik  ="))
                    a = float(input('masukan waktu ='))
                    tekanan(f,a)
                else:
                    print("trimakasih")
                    break
            
        case '16':
                 
                deltav = float(input("masukan jarak ="))
                deltat = float(input('masukan waktu tempuh ='))
                percepatan(deltav, deltat)
            
        case '17':
                m = float(input("masukan jarak ="))
                g = float(input('masukan waktu tempuh ='))
                deltah = float(input('masukan waktu tempuh ='))
                energipotensialgravitasi(m,g,deltah)
            
        case '18':
            while True:
                print("1. bola")
                print("2. Usaha")
                print("3. Keluar")
                
                pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                if pilihan == '1':
                    while True:
                        print("a. 3.14")
                        print("b. 22/7")
                        print("c. Keluar")
                
                        pilihan = str(input("pilihlah pi yang anda butuhkan (a/b/c) ="))

                        if pilihan == 'a':
                            r = float(input("masukan jari jari ="))
                            bola1(r)
                        
                        elif pilihan == 'b':
                            r = float(input("masukan jari jari ="))
                            bola2(r)
                        
                        else:
                            print("trimakasih")
                            break
                elif pilihan == '2':
                    while True:
                        print("a. 3.14")
                        print("b. 22/7")
                        print("c. Keluar")
                
                        pilihan = str(input("pilihlah pi yang anda butuhkan (a/b/c) ="))

                        if pilihan == 'a':
                            r = float(input("masukan jari jari ="))
                            h = float(input("masukan nilai ="))
                            s = float(input("masukan nilai ="))

                            kerucut1(r,h,s)
                        
                        elif pilihan == 'b':
                            r = float(input("masukan jari jari ="))
                            h = float(input("masukan nilai ="))
                            s = float(input("masukan nilai ="))

                            kerucut2(r,h,s)
                        
                        else:
                            print("trimakasih")
                            break
                
                elif pilihan == '3':
                    while True:
                            print("1. Perisma Segitiga Sama Sisi")
                            print("2. Perisma Segitiga sembarang")
                            print("3. Keluar")
                
                            pilihan = str(input("masukan pilihan yang anda (1/2/3) ="))

                            if pilihan == '1':
                                a = float(input("masukan jari jari ="))
                                p = float(input("masukan nilai ="))
                                t = float(input("masukan nilai ="))

                                Perisma_Segitiga_Sama_Sisi(a,p,t)
                        
                            elif pilihan == '2':
                                a = float(input("masukan jari jari ="))
                                p = float(input("masukan nilai ="))
                                t = float(input("masukan nilai ="))

                                Prisma_Segitiga_Sembarang(a,p,t)
                
                            else:
                                print("trimakasih")
                                break
        case '19':
            sudut = float(input("masukan sudut segitiga :"))
            kategori = kategorisegitiga(sudut)

        case '20':
            daftar =input("masukan dengan sepasi").split()
            angka = [int(angka)for angka in daftar]
            hasil = bilangan_ganjil(angka)
            print("hasil bilangan ganjil",hasil)
            
        
        case _:
            break
            



            



                    



    

            

            
    ulang = str(input("ulang lagi tidak? (ya/tidak)"))