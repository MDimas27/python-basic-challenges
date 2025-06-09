'''
✅ Challenge 1.3: Class Pegawai dan Manager

🎯 Tujuan:
Latihan inheritance dan method override (menimpa fungsi di parent class).
'''

class Pegawai:
    def __init__(self, nama, posisi, gaji_pokok):
        self.nama = nama
        self.posisi = posisi
        self.gaji_pokok = gaji_pokok
    
    def hitung_gaji_tahunan(self):
        return self.gaji_pokok * 12

class Manager(Pegawai):
    def __init__(self, nama, posisi, gaji_pokok, bonus_tahunan):
        super().__init__(nama, posisi, gaji_pokok)
        self.bonus_tahunan = bonus_tahunan
    
    def hitung_gaji_tahunan(self):
        return (self.gaji_pokok * 12) + self.bonus_tahunan
    
# Contoh Objek
pegawai1 = Pegawai("Budi", "Staff", 5000000)
manager1 = Manager("Siti", "Manager", 10000000, 2000000)

print(f"Gaji Tahunan {pegawai1.nama}: Rp{pegawai1.hitung_gaji_tahunan():,}")
print(f"Gaji Tahunan {manager1.nama}: Rp{manager1.hitung_gaji_tahunan():,}")