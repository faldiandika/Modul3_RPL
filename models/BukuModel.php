<?php
require_once "config/database.php";
class BukuModel {
 private $conn; private $table_name="buku";
 public function __construct() {
  $database=new Database(); $this->conn=$database->getConnection();
 }
 public function getAllBuku() {
  $stmt=$this->conn->prepare("SELECT * FROM buku"); $stmt->execute();
  return $stmt->fetchAll(PDO::FETCH_ASSOC);
 }
 public function getBukuById($id) {
  $stmt=$this->conn->prepare("SELECT * FROM buku WHERE id_buku=:id");
  $stmt->execute([":id"=>$id]); return $stmt->fetch(PDO::FETCH_ASSOC);
 }
 public function createBuku($judul,$penulis,$tahun_terbit) {
  $stmt=$this->conn->prepare("INSERT INTO buku (judul,penulis,tahun_terbit) VALUES (:judul,:penulis,:tahun)");
  return $stmt->execute([":judul"=>$judul,":penulis"=>$penulis,":tahun"=>$tahun_terbit]);
 }
 public function updateBuku($id,$judul,$penulis,$tahun_terbit) {
  $stmt=$this->conn->prepare("UPDATE buku SET judul=:judul,penulis=:penulis,tahun_terbit=:tahun WHERE id_buku=:id");
  return $stmt->execute([":id"=>$id,":judul"=>$judul,":penulis"=>$penulis,":tahun"=>$tahun_terbit]);
 }
 public function deleteBuku($id) {
  $stmt=$this->conn->prepare("DELETE FROM buku WHERE id_buku=:id");
  return $stmt->execute([":id"=>$id]);
 }
 public function getAllAnggota() {
  $stmt=$this->conn->prepare("SELECT * FROM anggota"); $stmt->execute();
  return $stmt->fetchAll(PDO::FETCH_ASSOC);
 }
 public function getAllPeminjaman() {
  $stmt=$this->conn->prepare("SELECT * FROM peminjaman"); $stmt->execute();
  return $stmt->fetchAll(PDO::FETCH_ASSOC);
 }
}
?>