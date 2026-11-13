import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.Buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        # Inisialisasi Model dan View
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        self.id_terpilih = None  # id_buku dari baris tabel yang diklik

        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_perbarui.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)

        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_perbarui.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():  # Mengosongkan isi tabel di View terlebih dahulu
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()  # Mengambil data dari Model (database)
        for buku in data_buku:  # Memasukkan data baru ke dalam tabel View
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')
        self.id_terpilih = None

    def pilih_baris(self, event=None):
        """Ambil id_buku dari baris yang diklik, lalu isi form dengan datanya."""
        pilihan = self.view.tabel.selection()
        if not pilihan:
            return

        nilai = self.view.tabel.item(pilihan[0])["values"]
        self.id_terpilih = nilai[0]  # kolom pertama = id_buku

        # Entry yang disabled (mode anggota) tidak bisa diisi, jadi lewati
        if self.user_role != "admin":
            return

        self.view.entry_judul.delete(0, 'end')
        self.view.entry_judul.insert(0, nilai[1])
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_penulis.insert(0, nilai[2])
        self.view.entry_tahun.delete(0, 'end')
        self.view.entry_tahun.insert(0, nilai[3])

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()  # Mengambil teks dari kotak input di View
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()  # Muat ulang tabel agar data terbaru muncul
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def perbarui_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk mengubah data!")
            return

        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih baris data di tabel terlebih dahulu!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # id_buku diteruskan ke BukuModel.update_buku
        if self.model.update_buku(self.id_terpilih, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih baris data di tabel terlebih dahulu!")
            return

        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            # id_buku diteruskan ke BukuModel.delete_buku
            if self.model.delete_buku(self.id_terpilih):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def logout(self):
        # Import di dalam fungsi untuk menghindari circular import
        # (auth_controller juga meng-import BukuController)
        from controllers.auth_controller import AuthController

        self.view.destroy()  # Tutup jendela perpustakaan
        AuthController().run()  # Kembali ke jendela LoginView

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()