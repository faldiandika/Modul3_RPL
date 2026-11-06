import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.Buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        # Inisialisasi Model dan View
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")
        
        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data) 

        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disable", text="Akses Terkunci (Khusu Admin)")
            self.view.entry_judul.configure(state="disable")
            self.view.entry_penulis.configure(state="disable")
            self.view.entry_tahun.configure(state="disable")

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():# Mengosongkan isi tabel di View terlebih dahulu
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()#Mengambil data dari Model (database)
        for buku in data_buku:# Memasukkan data baru ke dalam tabel View
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))
            
    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()# Mengambil teks dari kotak input di View
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        
        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
        
        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end') # Bersihkan form input
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()  # Muat ulang tabel agar data terbaru muncul
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()