<?php
require_once "models/BukuModel.php";

class BukuController {
    private $model;

    public function __construct() {
        $this->model = new BukuModel();
    }
    public function index() {
        $buku_list = $this->model->getAllBuku();
        $anggota_list = $this->model->getAllAnggota();
        $peminjaman_list = $this->model->getAllPeminjaman();
        $edit_buku = null;
        if (isset($_GET['aksi']) && $_GET['aksi'] === 'edit') {
            $edit_buku = $this->model->getBukuById($_GET['id']);
        }
        require_once "views/Buku_view.php";
    }
    public function tambah($judul, $penulis, $tahun) {
        if (!empty($judul) && !empty($penulis)) {
            $this->model->createBuku(
                $judul,
                $penulis,
                $tahun
            );
        }
        header("Location: index.php");
        exit;
    }
    public function ubah($id, $judul, $penulis, $tahun) {
        $this->model->updateBuku(
            $id,
            $judul,
            $penulis,
            $tahun
        );
        header("Location: index.php");
        exit;
    }
    public function hapus($id) {
        $this->model->deleteBuku($id);
        header("Location: index.php");
        exit;
    }
}
?>