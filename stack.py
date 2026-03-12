#data simulasi
data = [1, 2, 3, 5, 7, 10]

#menghitung banyaknya data
banyak_data = len(data)

#data yang dicari di tumpukan
yang_dicari = 2

#tumpukan_baru untuk hasil pindahan sementara 
tumpukan_baru = [0] * banyak_data

#nilai awal pointer tumpukan baru
hasil_ke = 0
 
#mencetak data mentah 
print (data)

print ( f"Banyaknya data : {banyak_data}")

print ( f"Data dicari: {yang_dicari}")

#looping dari data pertama-terakhir
for data_ke in range (banyak_data-1,-1,-1):
    #print (f"Data ke : {data_ke} {data[data_ke]}") 
    if (yang_dicari==data[data_ke]):
       print ("Ketemu")
       break
    else:
       #jika tidak sama, maka data disalin ke tumpukan baru
       tumpukan_baru[hasil_ke] = data[data_ke]
       #tumpukan baru bertambah satu
       hasil_ke += 1


#cetak tumpukan sementara setelah ketemu data yang dicari
for data_ke in range (hasil_ke-1,-1,-1):
    print (f"Tumpukan sementara : {data_ke+1} {tumpukan_baru[data_ke]}") 




