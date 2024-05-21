def hitungan_seri(hambatan):
    total_hambatan= sum(hambatan)
    return total_hambatan

n = int(input("masukan resistor yang ada ="))
hambatan_seri = []

for i in range(n):
    h = float(input(f"masukan nilai hambatan ke-{i+1}(ohm) ="))
    hambatan_seri.append(h)

total_hambatan_seri = hitungan_seri(hambatan_seri)
print("dadi {:.2f} ohm" .format(total_hambatan_seri))




while True:
                print("1. rangkaian seri ")
                print("2. rangkaian parallel ")
                print("3. keluar")

                pilihan = (input("masukan rangkaian yang anda butuhkan (1/2) :"))

                if pilihan == '1':
                    n = int(input("masukan jumlah resistor yang ada di rangkaian seri ="))
                    hambatan_seri = []

                    for i in range(n):
                        h = float(input(f"masukan nilai ke-{i+1}(ohm)"))
                        hambatan_seri.append(h)
                        total_hambatan_seri = hambatan_seri(hambatan_seri)
                        print("Hambatan total dalam rangkaian seri adalah{:.2f}ohm".format(total_hambatan_seri))
                
                elif pilihan == '2':
                    n = int(input("masukan jumlah resistor yang ada di rangkaian parallel ="))
                    hambatan_parallel = []

                    for i in range(n):
                        h = float(input(f"masukan nilai ke-{i+1}(ohm)"))
                        hambatan_parallel.append(h)
                        
                        total_hambatan_parallel = hambatan_total_parallel(hambatan_parallel)
                        print("Hambatan total dalam rangkaian parallel adalah{:.2f}ohm".format(total_hambatan_parallel))

                elif pilihan == 3:
                    print("trimakasih")
                    break

                else:
                    print("pilihan anda tidak di temukan")
            

        def hambatan_total_paralel(hambatan):
    total_hambatan = 0
    for h in hambatan:
        total_hambatan += 1 / h
    total_hambatan = 1 / total_hambatan
    return total_hambatan

def hambatan_total_parallel(hambatan_parallel):
    total_hambatan= 1 / sum(1/ hambatan_parallel)
    return total_hambatan