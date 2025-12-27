import tkinter as tk
from tkinter import messagebox

# 1. Inisialisasi Jendela Utama
window = tk.Tk()
window.title("Aplikasi GUI Sederhana")
window.geometry("300x250")

# --- FUNGSI ---

# Fungsi menampilkan isi Entry di messagebox (Gambar 4)
def tampilkan_pesan():
    isi_input = ent_input.get()
    messagebox.showinfo("Informasi", f"Isi Entry: {isi_input}")

# Fungsi untuk menghapus isi Entry (Gambar 3)
def hapus_entry():
    ent_input.delete(0, tk.END)

# --- KOMPONEN UI ---

# Label Instruksi (Gambar 2)
lbl_instruksi = tk.Label(window, text="Masukkan teks di bawah:")
lbl_instruksi.pack(pady=5)

# Entry Input (Gambar 2)
ent_input = tk.Entry(window)
ent_input.insert(0, "GELVI") # Mengisi default nama sesuai permintaan
ent_input.pack(pady=5)

# Button Tampilkan Pesan (Gambar 5)
btn_tampil = tk.Button(window, text="Tampilkan Pesan", command=tampilkan_pesan)
btn_tampil.pack(pady=5)

# Button Hapus Teks
btn_hapus = tk.Button(window, text="Hapus Teks", command=hapus_entry)
btn_hapus.pack(pady=5)

# Menjalankan Aplikasi
window.mainloop()