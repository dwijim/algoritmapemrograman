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
bilangan3 = int(input("Masukan bilangan ketiga: "))
bilangan4 = int(input("Masukan bilangan keempat: "))
bilangan5 = int(input("Masukan bilangan kelima: "))

terbesar = 10

if (bilangan1>terbesar):
    terbesar = bilangan1
if (bilangan2>terbesar):
    terbesar = bilangan2
if (bilangan3>terbesar):
    terbesar = bilangan3
if (bilangan4>terbesar):
    terbesar = bilangan4
if (bilangan5>terbesar):
    terbesar = bilangan5

print(f"Bilangan terbesar adalah {terbesar}.")


