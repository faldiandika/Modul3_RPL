import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():  # Kosongkan tabel dulu
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()  # Ambil data dari Model
        for anggota in data_anggota:
            # Cocok untuk kolom ID bernama id_anggota maupun id
            id_anggota = anggota.get("id_anggota", anggota.get("id"))
            self.view.tabel.insert("", "end", values=(id_anggota, anggota["nama"], anggota["alamat"]))

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Validasi Form Kosong
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.view.entry_nama.delete(0, 'end')  # Bersihkan form input
            self.view.entry_alamat.delete(0, 'end')
            self.muat_data_tabel()  # Muat ulang tabel
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()