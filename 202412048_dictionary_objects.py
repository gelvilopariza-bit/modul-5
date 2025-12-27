import tkinter as tk
from tkinter import ttk, messagebox

#  Class Pelanggan (dari image_2e90f3.png)
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

#  Class Aplikasi Utama 
class AplikasiManajemenPelanggan:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Pelanggan")
        self.root.geometry("600x450")

        # Dictionary untuk menyimpan data
        self.data_pelanggan = {}

        # --- UI Setup: Input Frame ---
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="ID Pelanggan:").grid(row=0, column=0, sticky=tk.W)
        self.entry_id = tk.Entry(frame_input, width=30)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Nama:").grid(row=1, column=0, sticky=tk.W)
        self.entry_nama = tk.Entry(frame_input, width=30)
        self.entry_nama.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.entry_email = tk.Entry(frame_input, width=30)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        # --- UI Setup: Tombol Frame ---
        frame_tombol = tk.Frame(root, padx=10, pady=5)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah Pelanggan", command=self.tambah_pelanggan).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus Pelanggan", command=self.hapus_pelanggan).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Cari Pelanggan", command=self.cari_pelanggan).pack(side=tk.LEFT, padx=5)

        # --- UI Setup: Tabel Frame  ---
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        kolom = ("id", "nama", "email")
        self.tabel = ttk.Treeview(frame_tabel, columns=kolom, show='headings')
        
        # Atur Header Tabel
        self.tabel.heading("id", text="ID Pelanggan")
        self.tabel.heading("nama", text="Nama")
        self.tabel.heading("email", text="Email")
        
        # Atur Lebar Kolom
        self.tabel.column("id", anchor=tk.CENTER)
        self.tabel.column("nama", anchor=tk.CENTER)
        self.tabel.column("email", anchor=tk.CENTER)
        
        self.tabel.pack(fill=tk.BOTH, expand=True)

    # --- Fungsi Logika ---
    def tambah_pelanggan(self):
        id_p = self.entry_id.get()
        nama = self.entry_nama.get()
        email = self.entry_email.get()

        if id_p and nama and email:
            if id_p not in self.data_pelanggan:
                pelanggan_baru = Pelanggan(id_p, nama, email)
                self.data_pelanggan[id_p] = pelanggan_baru
                self.update_tabel()
                self.bersihkan_input()
            else:
                messagebox.showwarning("Error", "ID Pelanggan sudah ada!")
        else:
            messagebox.showwarning("Error", "Semua kolom harus diisi!")

    def hapus_pelanggan(self):
        id_p = self.entry_id.get()
        if id_p in self.data_pelanggan:
            del self.data_pelanggan[id_p]
            self.update_tabel()
            self.bersihkan_input()
            messagebox.showinfo("Sukses", f"Pelanggan dengan ID {id_p} dihapus.")
        else:
            messagebox.showwarning("Error", "ID tidak ditemukan!")

    def cari_pelanggan(self):
        id_p = self.entry_id.get()
        if id_p in self.data_pelanggan:
            p = self.data_pelanggan[id_p]
            messagebox.showinfo("Hasil Cari", f"ID: {p.id_pelanggan}\nNama: {p.nama}\nEmail: {p.email}")
        else:
            messagebox.showwarning("Error", "Pelanggan tidak ditemukan!")

    def update_tabel(self):
        # Hapus semua data lama di tabel
        for item in self.tabel.get_children():
            self.tabel.delete(item)
        # Masukkan data baru dari dictionary
        for p in self.data_pelanggan.values():
            self.tabel.insert("", tk.END, values=(p.id_pelanggan, p.nama, p.email))

    def bersihkan_input(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

# Menjalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenPelanggan(root)
    root.mainloop()