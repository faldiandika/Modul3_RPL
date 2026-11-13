from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()


def test_get_all_buku():
    # Menginisialisasi Model
    model = BukuModel()

    # Data tiruan yang seolah-olah dikembalikan database
    data_dummy = [
        {"id_buku": 1, "judul": "Pemrograman Python", "penulis": "Budi", "tahun_terbit": 2023},
        {"id_buku": 2, "judul": "Basis Data MySQL", "penulis": "Sari", "tahun_terbit": 2022},
    ]

    # Memanipulasi (Mock) koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = data_dummy
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.get_all_buku()

    # Memverifikasi hasil berupa list dengan isi sesuai data tiruan
    assert isinstance(hasil, list)
    assert len(hasil) == 2
    assert hasil[0]["judul"] == "Pemrograman Python"
    # Memverifikasi query SELECT dijalankan dan cursor ditutup
    mock_cursor.execute.assert_called_once_with("SELECT * FROM buku")
    mock_cursor.close.assert_called_once()