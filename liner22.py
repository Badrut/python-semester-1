def solve_linear_equation(a1, b1, c1, a2, b2, c2):
    detA = a1 * b2 - a2 * b1
    
    if detA != 0:
        x = (c1 * b2 - c2 * b1) / detA
        y = (a1 * c2 - a2 * c1) / detA
        return x, y
    else:
        return None

a1 = float(input("masukan nilai ="))
b1 = float(input("masukan nilai ="))
c1 = float(input("masukan nilai ="))
a2 = float(input("masukan nilai ="))
b2 = float(input("masukan nilai ="))
c2 = float(input("masukan nilai ="))

solusi = solve_linear_equation(a1, b1, c1, a2, b2, c2)

if solusi:
    x, y = solusi
    print(f"Solusi x = {x}, y = {y}")
else:
    print("Sistem tidak memiliki solusi.")
