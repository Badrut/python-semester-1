def solusi_persamaan_linier(a, b):
    """
    Menyelesaikan persamaan linier satu variabel ax + b = 0.

    Parameters:
    a (float): Koefisien variabel x.
    b (float): Konstanta.

    Returns:
    float: Solusi x.
    """
    if a == 0:
        if b == 0:
            return "Infinite Solutions"  # Persamaan ini memiliki tak terbatas banyak solusi.
        else:
            return "No Solution"  # Persamaan ini tidak memiliki solusi.
    else:
        x = -b / a
        return x

# Contoh penggunaan:
a = float(input("masukan a ="))
b = float(input("masukan b ="))
solusi = solusi_persamaan_linier(a, b)

if isinstance(solusi, str):
    print(f"Hasil: {solusi}")
else:
    print(f"Nilai x: {solusi}")
