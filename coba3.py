def hambatan_total_seri(hambatan):
    total_hambatan = sum(hambatan)
    return total_hambatan

def hambatan_total_paralel(hambatan):
    total_hambatan = 1 / sum(1 / hambatan)
    return total_hambatan

# Menu utama
while True:
    print("Pilih jenis rangkaian:")
    print("1. Seri")
    print("2. Paralel")
    print("3. Keluar")
    
    pilihan = input("Masukkan nomor pilihan (1/2/3): ")

    if pilihan == "1":
        # Rangkaian Seri
        n = int(input("Masukkan jumlah resistor dalam rangkaian seri: "))
        hambatan_seri = []

        for i in range(n):
            h = float(input(f"Masukkan nilai hambatan ke-{i + 1} (ohm): "))
            hambatan_seri.append(h)

        total_hambatan_seri = hambatan_total_seri(hambatan_seri)
        print("Hambatan total dalam rangkaian seri adalah {:.2f} ohm".format(total_hambatan_seri))
    
    elif pilihan == "2":
        # Rangkaian Paralel
        n = int(input("Masukkan jumlah resistor dalam rangkaian paralel: "))
        hambatan_paralel = []

        for i in range(n):
            h = float(input(f"Masukkan nilai hambatan ke-{i + 1} (ohm): "))
            hambatan_paralel.append(h)

        total_hambatan_paralel = hambatan_total_paralel(hambatan_paralel)
        print("Hambatan total dalam rangkaian paralel adalah {:.2f} ohm".format(total_hambatan_paralel))
    
    elif pilihan == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Harap masukkan 1, 2, atau 3.")
