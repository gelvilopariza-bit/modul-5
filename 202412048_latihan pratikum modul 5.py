# Class Buku dengan atribut: judul, penulis, tahun.
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"'{self.judul}' oleh {self.penulis} ({self.tahun})"

# List yang berisi 5 objek buku.
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Sang Pemimpi", "Andrea Hirata", 2006),
    Buku("Filosofi Kopi", "Dee Lestari", 2006)
]

# Implementasi fungsi untuk mencari buku berdasarkan penulis.
def cari_buku_berdasarkan_penulis(list_buku, nama_penulis):
    hasil = [buku for buku in list_buku if nama_penulis.lower() in buku.penulis.lower()]
    return hasil

# Tampilan hasil pencarian.
penulis_dicari = "Andrea Hirata"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print(f"Hasil pencarian untuk penulis '{penulis_dicari}':")
if hasil_pencarian:
    for buku in hasil_pencarian:
        print(f"- {buku}")
else:
    print("Buku tidak ditemukan.")