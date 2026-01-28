print("="*45)
"""
Program Perhitungan Indeks Berat Badan (IMT)

Deskripsi:
    Program ini menghitung Indeks Massa Tubuh (IMT) berdasarkan input berat badan
    dan tinggi badan dari pengguna. Setelah perhitungan, program memberikan status
    kategori berat badan dan saran berdasarkan hasil IMT.

Input:
    - berat (float): Berat badan pengguna dalam kilogram (kg)
    - tinggi (float): Tinggi badan pengguna dalam meter (m)

Proses:
    - Menghitung IMT menggunakan rumus: IMT = berat / (tinggi ** 2)
    - Mengklasifikasikan status berat badan berdasarkan nilai IMT
    
Kategori IMT dan Status:
    - IMT < 18.5: Kekurangan Berat Badan
      * Saran: Tingkatkan asupan kalori dan nutrisi seimbang, konsultasi dengan ahli gizi
    - 18.5 <= IMT < 24.9: Berat Badan Normal
      * Saran: Pertahankan gaya hidup sehat dengan olahraga teratur dan diet seimbang
    - 25 <= IMT < 29.9: Kelebihan Berat Badan
      * Saran: Kurangi asupan kalori, tingkatkan aktivitas fisik, dan konsultasi dokter
    - IMT >= 30: Obesitas
      * Saran: Segera konsultasi dengan dokter atau ahli gizi untuk program penurunan berat badan

Output:
    - Berat badan (kg)
    - Tinggi badan (m)
    - Nilai IMT (dengan 2 desimal)
    - Status kategori berat badan
    - Saran kesehatan berdasarkan status

Return:
    None (Program hanya menampilkan output ke layar)
"""
print("=== Program Perhitungan Indeks Berat Badan ===")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

imt = berat / (tinggi ** 2)

print(f"Berat Badan: {berat} kg")
print(f"Tinggi Badan: {tinggi} m")
print(f"Indeks Berat Badan (IMT): {imt:.2f}")
if imt < 18.5:
    status = "Kekurangan Berat Badan"
elif 18.5 <= imt < 24.9:
    status = "Berat Badan Normal"
elif 25 <= imt < 29.9:
    status = "Kelebihan Berat Badan"
else:
    status = "Obesitas" 
print(f"Status: {status}")
print("="*45)
print("=== Terima kasih telah menggunakan program ini ===")
print("="*45)

if imt < 18.5:
    saran = "Tingkatkan asupan kalori dan nutrisi seimbang, konsultasi dengan ahli gizi"
elif 18.5 <= imt < 24.9:
    saran = "Pertahankan gaya hidup sehat dengan olahraga teratur dan diet seimbang"
elif 25 <= imt < 29.9:
    saran = "Kurangi asupan kalori, tingkatkan aktivitas fisik, dan konsultasi dokter"
else:
    saran = "Segera konsultasi dengan dokter atau ahli gizi untuk program penurunan berat badan"

print(f"Saran: {saran}")
