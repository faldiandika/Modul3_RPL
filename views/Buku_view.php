<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Sistem Perpustakaan</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        h1 { font-size: 22px; } h2 { font-size: 18px; margin-top: 18px; }
        input, button { padding: 6px; }
        table { border-collapse: collapse; margin-bottom: 18px; }
        th, td { border: 1px solid #777; padding: 5px 8px; font-size: 12px; }
        th { background: #eee; } a { color: blue; margin-right: 8px; }
        .form-row { display: flex; gap: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Sistem Perpustakaan</h1>
    <p>Pengelolaan data buku, anggota, dan peminjaman</p>

    <?php if ($edit_buku): ?>
        <h2>Edit Data Buku</h2>
        <form action="index.php" method="POST">
            <input type="hidden" name="aksi" value="ubah">
            <input type="hidden" name="id" value="<?= $edit_buku['id_buku']; ?>">
            <div class="form-row">
                <input type="text" name="judul" value="<?= htmlspecialchars($edit_buku['judul']); ?>" placeholder="Judul Buku" required>
                <input type="text" name="penulis" value="<?= htmlspecialchars($edit_buku['penulis']); ?>" placeholder="Penulis" required>
                <input type="number" name="tahun" value="<?= $edit_buku['tahun_terbit']; ?>" placeholder="Tahun Terbit" required>
                <button type="submit">Simpan Perubahan</button>
            </div>
        </form>
    <?php else: ?>
        <h2>Tambah Data Buku</h2>
        <form action="index.php" method="POST">
            <input type="hidden" name="aksi" value="tambah">
            <div class="form-row">
                <input type="text" name="judul" placeholder="Judul Buku" required>
                <input type="text" name="penulis" placeholder="Penulis" required>
                <input type="number" name="tahun" placeholder="Tahun Terbit" required>
                <button type="submit">Tambah Buku</button>
            </div>
        </form>
    <?php endif; ?>

    <h2>Daftar Koleksi Buku</h2>
    <table>
        <tr><th>ID</th><th>Judul Buku</th><th>Penulis</th><th>Tahun Terbit</th><th>Aksi</th></tr>
        <?php foreach ($buku_list as $buku): ?>
        <tr>
            <td><?= $buku['id_buku']; ?></td>
            <td><?= htmlspecialchars($buku['judul']); ?></td>
            <td><?= htmlspecialchars($buku['penulis']); ?></td>
            <td><?= $buku['tahun_terbit']; ?></td>
            <td><a href="index.php?aksi=edit&id=<?= $buku['id_buku']; ?>">Edit</a>
                <a href="index.php?aksi=hapus&id=<?= $buku['id_buku']; ?>" onclick="return confirm('Yakin ingin menghapus buku ini?')">Hapus</a></td>
        </tr>
        <?php endforeach; ?>
    </table>

    <h2>Daftar Anggota</h2>
    <table>
        <tr><th>ID Anggota</th><th>Nama</th><th>Alamat</th></tr>
        <?php foreach ($anggota_list as $anggota): ?>
        <tr><td><?= $anggota['id_anggota']; ?></td><td><?= htmlspecialchars($anggota['nama']); ?></td><td><?= htmlspecialchars($anggota['alamat']); ?></td></tr>
        <?php endforeach; ?>
    </table>

    <h2>Daftar Peminjaman</h2>
    <table>
        <tr><th>ID Pinjam</th><th>ID Buku</th><th>ID Anggota</th><th>Tanggal Pinjam</th><th>Tanggal Kembali</th></tr>
        <?php foreach ($peminjaman_list as $pinjam): ?>
        <tr><td><?= $pinjam['id_pinjam']; ?></td><td><?= $pinjam['id_buku']; ?></td><td><?= $pinjam['id_anggota']; ?></td><td><?= $pinjam['tanggal_pinjam']; ?></td><td><?= $pinjam['tanggal_kembali']; ?></td></tr>
        <?php endforeach; ?>
    </table>
</body>
</html>