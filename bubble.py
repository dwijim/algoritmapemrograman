# program pengurutan data dengan bubble sort

# fungsi bubble sort
def bubble_sort(datanya):

    # hitung ukuran data
    ukuran = len(datanya)
    
    # proses pengurutan
    for proses in range(ukuran):
        # proses pengurutan
        for ke  in range(0, ukuran - proses - 1):
            # jika data yang diurutkan lebih besar dari data yang diurutkan selanjutnya
            if datanya[ke] > datanya[ke + 1]:
                # maka ditukar yang kanan dengan yang kiri
                datanya[ke], datanya[ke + 1] = datanya[ke + 1], datanya[ke]
                
    # kembalikan data yang sudah diurutkan
    return datanya

# Contoh
data = [5, 3, 8, 1, 2]
print("Data sebelum diurutkan:")
print(data)
print("Data setelah diurutkan:")
print(bubble_sort(data)) 
