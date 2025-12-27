import tkinter as tk
from tkinter import messagebox

# Objek untuk merepresentasikan Tugas
class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.selesai = False

    def __str__(self):
        status = "[SELESAI]" if self.selesai else "[BELUM]"
        return f"{status} {self.deskripsi}"

# Aplikasi GUI untuk manajemen tugas
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Manajemen Tugas (To-Do List)")
        self.root.geometry("400x450")

        # List of objects untuk menyimpan data tugas
        self.daftar_objek_tugas = []

        # Komponen Antarmuka
        self.label = tk.Label(root, text="Masukkan Tugas Baru:", font=("Arial", 10))
        self.label.pack(pady=5)

        self.entry_tugas = tk.Entry(root, width=40)
        self.entry_tugas.pack(pady=5)

        # Frame untuk tombol-tombol aksi
        frame_tombol = tk.Frame(root)
        frame_tombol.pack(pady=10)

        # Implementas fitur: tambah, hapus, edit, dan tandai selesai
        self.btn_tambah = tk.Button(frame_tombol, text="Tambah", command=self.tambah_tugas, width=10)
        self.btn_tambah.grid(row=0, column=0, padx=5)

        self.btn_edit = tk.Button(frame_tombol, text="Edit", command=self.edit_tugas, width=10)
        self.btn_edit.grid(row=0, column=1, padx=5)

        self.btn_selesai = tk.Button(frame_tombol, text="Selesai", command=self.tandai_selesai, width=10, bg="#90ee90")
        self.btn_selesai.grid(row=1, column=0, padx=5, pady=5)

        self.btn_hapus = tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas, width=10, bg="red", fg="white")
        self.btn_hapus.grid(row=1, column=1, padx=5, pady=5)

        # Listbox untuk menampilkan daftar tugas
        self.listbox_tugas = tk.Listbox(root, width=45, height=15)
        self.listbox_tugas.pack(pady=10, padx=10)

    def perbarui_tampilan(self):
        """Menyegarkan Listbox berdasarkan isi daftar_objek_tugas"""
        self.listbox_tugas.delete(0, tk.END)
        for tugas in self.daftar_objek_tugas:
            self.listbox_tugas.insert(tk.END, str(tugas))

    def tambah_tugas(self):
        deskripsi = self.entry_tugas.get()
        if deskripsi:
            tugas_baru = Tugas(deskripsi)
            self.daftar_objek_tugas.append(tugas_baru)
            self.perbarui_tampilan()
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")

    def edit_tugas(self):
        try:
            index = self.listbox_tugas.curselection()[0]
            deskripsi_baru = self.entry_tugas.get()
            if deskripsi_baru:
                self.daftar_objek_tugas[index].deskripsi = deskripsi_baru
                self.perbarui_tampilan()
                self.entry_tugas.delete(0, tk.END)
            else:
                messagebox.showwarning("Peringatan", "Masukkan teks baru di kotak input untuk mengedit!")
        except IndexError:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diedit!")

    def tandai_selesai(self):
        try:
            index = self.listbox_tugas.curselection()[0]
            self.daftar_objek_tugas[index].selesai = True
            self.perbarui_tampilan()
        except IndexError:
            messagebox.showwarning("Peringatan", "Pilih tugas yang sudah selesai!")

    def hapus_tugas(self):
        try:
            index = self.listbox_tugas.curselection()[0]
            del self.daftar_objek_tugas[index]
            self.perbarui_tampilan()
        except IndexError:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()