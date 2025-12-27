import tkinter as tk
from tkinter import messagebox

# Class untuk mengorganisir komponen GUI
class AplikasiKonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Celsius ke Fahrenheit")
        self.root.geometry("350x200")

        # Membuat Komponen GUI
        self.label_instruksi = tk.Label(root, text="Masukkan suhu dalam Celsius:")
        self.label_instruksi.pack(pady=10)

        self.entry_celsius = tk.Entry(root)
        self.entry_celsius.pack(pady=5)

        self.btn_konversi = tk.Button(root, text="Konversi", command=self.konversi)
        self.btn_konversi.pack(pady=10)

        self.label_hasil = tk.Label(root, text="Hasil: -", font=("Helvetica", 10, "bold"))
        self.label_hasil.pack(pady=10)

    # Fungsi untuk konversi suhu
    def konversi(self):
        input_user = self.entry_celsius.get()

        # Validasi input
        try:
            # Mencoba mengubah input menjadi angka (float)
            celsius = float(input_user)

            # Rumus: F = (C * 9/5) + 32
            fahrenheit = (celsius * 9/5) + 32

            # Menampilkan hasil
            self.label_hasil.config(text=f"Hasil: {fahrenheit:.2f} °F")

        except ValueError:
            # Jika input bukan angka, tampilkan peringatan
            messagebox.showerror("Error", "Mohon masukkan angka yang valid!")
            self.entry_celsius.delete(0, tk.END)

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKonversiSuhu(root)
    root.mainloop()