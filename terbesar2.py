import os

# program dalam bahasa python
# nama file : terbesar2.py
# dijalankan dengan perintah ptyhon3 terbesar2.py


#menghapus layar di Linux pakai clear
#kalau di windows pakai cls
os.system('clear')

# pemasukan data  
bilangan1 = int(input("Masukan bilangan pertama: "))
bilangan2 = int(input("Masukan bilangan kedua: "))

if (bilangan1>bilangan2):
    terbesar = bilangan1
else:    
    terbesar = bilangan2

print(f"Bilangan terbesar adalah {terbesar}.")


