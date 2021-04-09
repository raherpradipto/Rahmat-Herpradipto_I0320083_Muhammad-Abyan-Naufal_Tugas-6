# program nilai rata-rata

# input jumlah nilai
total_nilai = []
jumlah_nilai = int(input("Masukkan jumlah nilai : "))

# input nilai
r = 1
while r <= jumlah_nilai:
    nilai = float(input("Masukkan nilai ke-%d: " % r))
    total_nilai.append(nilai)
    r = r + 1

# output nilai rata-rata
nilai_rata2 = sum(total_nilai)/jumlah_nilai
print("Nilai rata-rata adalah : ", nilai_rata2)
