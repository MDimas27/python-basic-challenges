'''
✅ Challenge 1.2: Class Buku dan Majalah dengan Inheritance

🎯 Tujuan:
Latihan OOP (Object-Oriented Programming) dan konsep inheritance.
'''

class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def display_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
    
class Majalah(Buku):
    def __init__(self, judul, penulis, tahun_terbit, edisi, bulan_terbit):
        super().__init__(judul, penulis, tahun_terbit)
        self.edisi = edisi
        self.bulan_terbit = bulan_terbit

    def display_info(self):
        super().display_info()
        print(f"Edisi: {self.edisi}")
        print(f"Bulan Terbit: {self.bulan_terbit}")

# Contoh objek
buku1 = Buku("Pemroigraman Python", "Andi", 2022)
majalah1 = Majalah("Tekno Weekly", "Dewi", 2023, "Vol. 5", "Januari")

buku1.display_info()
print("\n---\n")
majalah1.display_info()
