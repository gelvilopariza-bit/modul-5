class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def info(self):
        return f"{self.nama} (NIM: {self.nim}) - IPK: {self.ipk}"

# Membuat list of objects
daftar_mahasiswa = [
    Mahasiswa("Ahmad", "IT001", 3.5),
    Mahasiswa("Budi", "IT002", 3.2),
    Mahasiswa("Citra", "IT003", 3.8)
]

# Mengakses list of objects
print("=== Daftar Mahasiswa ===")
for mhs in daftar_mahasiswa:
    print(mhs.info())

# Filter berdasarkan IPK
print("\n=== Mahasiswa dengan IPK > 3.5 ===")
for mhs in daftar_mahasiswa:
    if mhs.ipk > 3.5:
        print(mhs.info())