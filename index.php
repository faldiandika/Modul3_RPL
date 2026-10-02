<?php

require_once "controllers/Bukucontroller.php";

$controller = new BukuController();


// TAMBAH BUKU
if (
    $_SERVER['REQUEST_METHOD'] === 'POST'
    && isset($_POST['aksi'])
    && $_POST['aksi'] === 'tambah'
) {

    $controller->tambah(
        $_POST['judul'],
        $_POST['penulis'],
        $_POST['tahun']
    );

}


// UBAH BUKU
elseif (
    $_SERVER['REQUEST_METHOD'] === 'POST'
    && isset($_POST['aksi'])
    && $_POST['aksi'] === 'ubah'
) {

    $controller->ubah(
        $_POST['id'],
        $_POST['judul'],
        $_POST['penulis'],
        $_POST['tahun']
    );

}


// HAPUS BUKU
elseif (
    isset($_GET['aksi'])
    && $_GET['aksi'] === 'hapus'
) {

    $controller->hapus($_GET['id']);

}


// TAMPILKAN HALAMAN
else {

    $controller->index();

}

?>