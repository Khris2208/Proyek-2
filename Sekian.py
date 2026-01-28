print("=== Program Perhitungan Indeks Berat Badan ===")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

imt = berat / (tinggi ** 2)

print(f"Berat Badan: {berat} kg")
print(f"Tinggi Badan: {tinggi} m")
print(f"Indeks Berat Badan (IMT): {imt:.2f}")