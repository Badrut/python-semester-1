def solve_linear_equation(a1, b1, c1, a2, b2, c2):
    # Matriks koefisien
    A = [[a1, b1], [a2, b2]]
    
    # Vektor konstanta
    B = [c1, c2]

    # Menemukan determinan matriks koefisien
    detA = a1 * b2 - a2 * b1

    # Cek apakah sistem memiliki solusi tunggal (determinan tidak sama dengan 0)
    if detA != 0:
        # Menyelesaikan matriks menggunakan eliminasi Gauss
        x = (B[0] * b2 - B[1] * b1) / detA
        y = (a1 * B[1] - a2 * B[0]) / detA
        return x, y
    else:
        return None  # Sistem tidak memiliki solusi

# Contoh pemanggilan fungsi untuk menyelesaikan persamaan:
a1 = float(input("Masukan angka pertama ="))
b1 = float(input("Masukan angka kedua ="))
c1 = float(input("Masukan angka ketiga ="))
a2 = float(input("Masukan angka keempat ="))
b2 = float(input("Masukan angka kelima ="))
c2 = float(input("Masukan angka keenam ="))

solusi = solve_linear_equation(a1, b1, c1, a2, b2, c2)

if solusi:
    x, y = solusi
    print(f"Solusi x = {x}, y = {y}")
else:
    print("Sistem tidak memiliki solusi.")
