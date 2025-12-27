import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# 1. Class Mahasiswa
class Mahasiswa:
    """
    Class Mahasiswa
    Atribut:
    - nim
    - nama
    - jurusan
    - ipk
    """
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def info(self):
        """Mengembalikan data mahasiswa dalam bentuk tuple"""
        return (self.nim, self.nama, self.jurusan, self.ipk)

    def update_ipk(self, ipk_baru):
        """Mengupdate IPK mahasiswa"""
        self.ipk = float(ipk_baru)

# 2. Class Aplikasi Utama
class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Data Mahasiswa")
        self.root.geometry("850x500")

        # Dictionary untuk menyimpan objek mahasiswa dengan NIM sebagai key
        self.data_mahasiswa = {}

        self.buat_gui()

    def buat_gui(self):
        # a. Frame Input Data
        frame_input = tk.LabelFrame(self.root, text="Input Data Mahasiswa")
        frame_input.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0, padx=5, pady=5)
        self.ent_nim = tk.Entry(frame_input)
        self.ent_nim.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Nama").grid(row=0, column=2, padx=5, pady=5)
        self.ent_nama = tk.Entry(frame_input)
        self.ent_nama.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_input, text="Jurusan").grid(row=1, column=0, padx=5, pady=5)
        self.ent_jurusan = tk.Entry(frame_input)
        self.ent_jurusan.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="IPK").grid(row=1, column=2, padx=5, pady=5)
        self.ent_ipk = tk.Entry(frame_input)
        self.ent_ipk.grid(row=1, column=3, padx=5, pady=5)

        # b. Tombol Operasi CRUD
        frame_button = tk.Frame(self.root)
        frame_button.pack(fill="x", pady=5)

        tk.Button(frame_button, text="Tambah", command=self.tambah_data).pack(side="left", padx=5)
        tk.Button(frame_button, text="Update", command=self.update_data).pack(side="left", padx=5)
        tk.Button(frame_button, text="Hapus", command=self.hapus_data).pack(side="left", padx=5)
        tk.Button(frame_button, text="Export", command=self.export_data).pack(side="right", padx=5)

        # Fitur Cari & Filter
        frame_cari = tk.Frame(self.root)
        frame_cari.pack(fill="x", padx=10)
        
        tk.Label(frame_cari, text="Cari (NIM/Nama)").pack(side="left")
        self.ent_cari = tk.Entry(frame_cari)
        self.ent_cari.pack(side="left", padx=5)
        tk.Button(frame_cari, text="Cari", command=self.cari_data).pack(side="left")

        tk.Label(frame_cari, text="Filter Jurusan").pack(side="left", padx=(20,0))
        self.ent_filter = tk.Entry(frame_cari)
        self.ent_filter.pack(side="left", padx=5)
        tk.Button(frame_cari, text="Filter", command=self.filter_jurusan).pack(side="left")

        # c. Treeview (Tampilan Data)
        self.tree = ttk.Treeview(
            self.root, 
            columns=("NIM", "Nama", "Jurusan", "IPK"), 
            show="headings"
        )
        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.heading("IPK", text="IPK")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Label Statistik
        self.lbl_info = tk.Label(self.root, text="", fg="blue")
        self.lbl_info.pack(pady=5)

    # Logika Fungsi
    def validasi_input(self):
        """Validasi input agar tidak kosong dan IPK angka"""
        if not all([self.ent_nim.get(), self.ent_nama.get(), self.ent_jurusan.get(), self.ent_ipk.get()]):
            return False
        return True

    def tambah_data(self):
        if self.validasi_input():
            nim = self.ent_nim.get()
            mhs = Mahasiswa(nim, self.ent_nama.get(), self.ent_jurusan.get(), self.ent_ipk.get())
            self.data_mahasiswa[nim] = mhs
            self.refresh_table()
            self.hitung_ipk()
        else:
            messagebox.showwarning("Input Salah", "Semua kolom harus diisi!")

    def update_data(self):
        nim = self.ent_nim.get()
        if nim in self.data_mahasiswa:
            self.data_mahasiswa[nim].nama = self.ent_nama.get()
            self.data_mahasiswa[nim].jurusan = self.ent_jurusan.get()
            self.data_mahasiswa[nim].update_ipk(self.ent_ipk.get())
            self.refresh_table()
            self.hitung_ipk()

    def hapus_data(self):
        nim = self.ent_nim.get()
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            self.refresh_table()
            self.hitung_ipk()

    def refresh_table(self, data_list=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        display_data = data_list if data_list is not None else self.data_mahasiswa.values()
        for mhs in display_data:
            self.tree.insert("", "end", values=mhs.info())

    def cari_data(self):
        """Pencarian berdasarkan NIM atau Nama"""
        keyword = self.ent_cari.get().lower()
        hasil = [
            mhs for mhs in self.data_mahasiswa.values()
            if keyword in mhs.nim.lower() or keyword in mhs.nama.lower()
        ]
        self.refresh_table(hasil)

    def filter_jurusan(self):
        """Filter mahasiswa berdasarkan jurusan"""
        jurusan = self.ent_filter.get().lower()
        hasil = [
            mhs for mhs in self.data_mahasiswa.values()
            if jurusan in mhs.jurusan.lower()
        ]
        self.refresh_table(hasil)

    def hitung_ipk(self):
        """Menghitung rata-rata dan IPK tertinggi"""
        if not self.data_mahasiswa:
            self.lbl_info.config(text="")
            return
        
        total_ipk = sum(mhs.ipk for mhs in self.data_mahasiswa.values())
        rata_rata = total_ipk / len(self.data_mahasiswa)
        mhs_tertinggi = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        
        text = f"Rata-rata IPK: {rata_rata:.2f} | IPK Tertinggi: {mhs_tertinggi.nama} ({mhs_tertinggi.ipk})"
        self.lbl_info.config(text=text)

    def export_data(self):
        """Export data mahasiswa ke file teks"""
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for mhs in self.data_mahasiswa.values():
                    f.write(f"{mhs.nim}, {mhs.nama}, {mhs.jurusan}, {mhs.ipk}\n")
            messagebox.showinfo("Sukses", "Data berhasil diexport!")

# PROGRAM UTAMA
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop() 