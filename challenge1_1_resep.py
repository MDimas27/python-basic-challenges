'''
✅ Challenge 1.1: Sistem Manajemen Resep Sederhana

🎯 Tujuan:
Latihan manipulasi data dengan list, dictionary, dan fungsi.

🧠 Konsep Dasar:
Dictionary untuk menyimpan 1 resep: {'nama': ..., 'bahan': [...], 'langkah': [...]}.
List untuk menyimpan banyak resep.
Fungsi modular untuk CRUD sederhana.

'''

# List untuk menyimpan semua resep
daftar_resep = []

def tambah_resep(nama, bahan, langkah):
    resep = {
        'nama': nama,
        'bahan': bahan,
        'langkah': langkah
    }
    daftar_resep.append(resep)
    print(f"Resep '{nama}' berhasil ditambahkan!")

def tampilkan_semua_resep():
    for i, resep in enumerate(daftar_resep, start=1):
        print(f"\nResep {i}: {resep['nama']}")
        print(" Bahan:")
        for b in resep['bahan']:
            print(f"  - {b}")
        print(" Langkah:")
        for l in resep['langkah']:
            print(f"  - {l}")

def cari_resep_berdasarkan_bahan(keyword):
    hasil = []
    for resep in daftar_resep:
        if keyword.lower() in [b.lower() for b in resep['bahan']]:
            hasil.append(resep)
    if hasil:
        print(f"\nDitemukan {len(hasil)} resep yang mengandung bahan '{keyword}':")
        for resep in hasil:
            print(f"  - {resep['nama']}")
    else:
        print(f"Tidak ada resep dengan bahan '{keyword}'.")

# Contoh penggunaan
tambah_resep("Nasi Goreng", ["nasi", "telur", "kecap", "bawang"], ["Tumis bawang", "Masukkan telur", "Masukkan nasi & kecap", "Aduk rata"])
tambah_resep("Mie Rebus", ["mie", "air", "bumbu", "telur"], ["Rebus air", "Masukkan mie", "Tambahkan telur & bumbu", "Masak sampai matang"])


tampilkan_semua_resep()
cari_resep_berdasarkan_bahan("air")
