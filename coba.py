


# Fungsi untuk mencari bilangan ganjil dalam daftar
def cari_bilangan_ganjil(daftar):
    bilangan_ganjil = []  # Inisialisasi daftar kosong untuk menyimpan bilangan ganjil
    
    for angka in daftar:
        if angka % 2 != 0:  # Periksa apakah angka tersebut ganjil
            bilangan_ganjil.append(angka)  # Jika ganjil, tambahkan ke daftar bilangan_ganjil
            
    return bilangan_ganjil  # Kembalikan daftar bilangan ganjil

# Input dari pengguna
input_daftar = input("Masukkan daftar angka (pisahkan dengan spasi): ").split()
daftar_angka = [int(angka) for angka in input_daftar]  # Mengonversi input ke dalam daftar angka

# Panggil fungsi untuk mencari bilangan ganjil
hasil = cari_bilangan_ganjil(daftar_angka)

# Cetak hasil
print("Bilangan Ganjil dalam Daftar:", hasil)






    











