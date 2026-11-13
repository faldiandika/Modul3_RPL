# Sistem Manajemen Perpustakaan

Aplikasi desktop manajemen perpustakaan berbasis Python dengan arsitektur **MVC (Model-View-Controller)**. Antarmuka dibuat dengan **CustomTkinter**, data disimpan di **MySQL**.

## Fitur

- Login dengan password ter-hash **SHA-256**
- Otorisasi berbasis role:
  - **admin**: tambah, perbarui, dan hapus data buku
  - **anggota**: hanya melihat data (tombol Simpan, Perbarui, Hapus terkunci)
- Manajemen data buku (CRUD) dan daftar anggota
- Tombol Logout kembali ke jendela Login
- Unit test dengan **pytest** dan pengecekan kode dengan **flake8** di GitHub Actions

## Struktur Direktori MVC

```
Modul_3/
├── main.py                   # Titik masuk aplikasi
├── requirements.txt          # Daftar dependensi
├── config/
│   └── database.py           # Koneksi ke MySQL
├── models/                   # MODEL: akses data dan logika bisnis
│   ├── buku_model.py
│   ├── anggota_model.py
│   └── user_model.py
├── views/                    # VIEW: tampilan GUI
│   ├── login_view.py
│   ├── Buku_view.py
│   └── anggota_view.py
├── controllers/              # CONTROLLER: penghubung View dan Model
│   ├── auth_controller.py
│   ├── buku_controller.py
│   └── anggota_controller.py
└── tests/
    └── test_buku.py          # Unit test (pytest)
```

CI pipeline ada di `.github/workflows/ci_pipeline.yml` (menjalankan flake8 lalu pytest).

## Instalasi dan Konfigurasi Database MySQL

### 1. Prasyarat

- Python 3.11 atau lebih baru
- MySQL / MariaDB (contoh: Laragon)
- Git

### 2. Clone repositori

```
git clone https://github.com/faldiandika/Modul3_RPL.git
cd Modul3_RPL/Modul_3
```

### 3. Instal dependensi

```
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 4. Siapkan database MySQL

1. Jalankan MySQL (di Laragon klik **Start All**).
2. Buat database baru bernama `GANTI_NAMA_DATABASE`.
3. Buat tabel yang dipakai aplikasi:

| Tabel | Kolom yang dipakai aplikasi |
|---|---|
| `buku` | `id_buku`, `judul`, `penulis`, `tahun_terbit` |
| `anggota` | kolom ID, `nama`, `alamat` |
| `users` | `id_user`, `username`, `password` (hash SHA-256), `role` |

4. Sesuaikan koneksi di `config/database.py` (host, user, password, dan nama database).

### 5. Buat akun pengguna

Password disimpan dalam bentuk hash, jadi buat akun lewat `register_user`:

```
python -c "from models.user_model import UserModel; print(UserModel().register_user('admin', 'password123', 'admin'))"
```

Ganti `admin` dan `password123` sesuai kebutuhan. Role yang dikenali: `admin` dan `anggota`.

## Cara Menjalankan Aplikasi

Dari folder `Modul_3` dengan environment aktif:

```
python main.py
```

Login dengan akun yang sudah dibuat. Untuk menutup sesi, klik **Logout**.

### Menjalankan tes

```
python -m pytest tests/test_buku.py -v
```

### Pengecekan kualitas kode

```
python -m flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

### Versi executable

Unduh `AplikasiPerpustakaan.exe` dari halaman **Releases** repositori ini, lalu jalankan. MySQL harus aktif dan konfigurasinya sesuai.