from models.anggota_model import AnggotaModel

anggota_model = AnggotaModel()

print("Menambahkan data anggota...")
anggota_model.create_anggota("Trian", "Jln. Untad 1")
print("Data anggota berhasil disimpan ke Laragon MySQL!")

print("\n" + "="*40 + "\n")

print("=== Daftar Anggota ===")
daftar_anggota = anggota_model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")