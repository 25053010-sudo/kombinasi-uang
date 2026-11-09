def pencarian_kombinasi(pecahan, target):
hasil = []

def cari(index, sisa, kombinasi):

if sisa == 0:
hasil.append(kombinasi.copy())
return

if index == len(pecahan):
return
uang = pecahan[index]
for jumlah in range(sisa // uang + 1):
kombinasi.append(jumlah)
cari(
index + 1,
sisa - (jumlah * uang),
Kombinasi)
kombinasi.pop()
cari(0, target, [])
return hasil
pecahan = [10000, 5000, 2000, 1000]
target = 10000
hasil = pencarian_kombinasi(pecahan, target)
print("================================")
print(" PENCARIAN KOMBINASI UANG")
print("================================")
print("Nominal Target : Rp", target)
print("Jumlah Kombinasi:", len(hasil))
print("--------------------------------")
for nomor, kombinasi in enumerate(hasil, 1):
rincian = []

for uang, jumlah in zip(pecahan, kombinasi):

if jumlah > 0:
rincian.append(
f"{jumlah} x Rp{uang:,}".replace(",", "."))

print(f"{nomor}. " + " + ".join(rincian))

print("--------------------------------")
print("Pencarian kombinasi selesai.")

