# program perulangan turun

# data yang akan diolah
data = [10, 20, 30, 40, 50]

# data yang akan dicari
cari_data = 300

# hitung jumlah data
n = len(data)

# Loop dari index terakhir (n-1) sampai 0
for i in range(n - 1, -1, -1):
    print(f"Index {i}: {data[i]}")
    if data[i] == cari_data:
        print(f"Data {cari_data} ditemukan pada index {i}")
        break
else:
        print(f"Data {cari_data} tidak ditemukan")


