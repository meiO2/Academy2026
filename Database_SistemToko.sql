-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Waktu pembuatan: 02 Bulan Mei 2025 pada 06.22
-- Versi server: 9.1.0
-- Versi PHP: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tokobogajaya`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang`
--

DROP TABLE IF EXISTS `barang`;
CREATE TABLE IF NOT EXISTS `barang` (
  `ID_BARANG` varchar(5) NOT NULL,
  `Nama_Barang` varchar(100) DEFAULT NULL,
  `Jumlah_Barang` int DEFAULT NULL,
  `Stok_Barang` int DEFAULT NULL,
  `Harga_Jual` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_BARANG`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `barang`
--

INSERT INTO `barang` (`ID_BARANG`, `Nama_Barang`, `Jumlah_Barang`, `Stok_Barang`, `Harga_Jual`) VALUES
('B0001', 'Tepung Tapioka Rose Brand 500gr', 200, 150, 9200.00),
('B0002', 'Palmia Serbaguna Sachet 200gr', 300, 200, 6800.00);

-- --------------------------------------------------------

--
-- Struktur dari tabel `detail_pemasokan`
--

DROP TABLE IF EXISTS `detail_pemasokan`;
CREATE TABLE IF NOT EXISTS `detail_pemasokan` (
  `ID_PEMASOK` varchar(5) NOT NULL,
  `ID_BARANG` varchar(5) NOT NULL,
  `Tanggal` datetime DEFAULT CURRENT_TIMESTAMP,
  `Jumlah` int DEFAULT NULL,
  `Harga` float(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_BARANG`,`ID_PEMASOK`,`Tanggal`),
  KEY `ID_PEMASOK` (`ID_PEMASOK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `detail_pemasokan`
--

INSERT INTO `detail_pemasokan` (`ID_PEMASOK`, `ID_BARANG`, `Tanggal`, `Jumlah`, `Harga`) VALUES
('PK001', 'B0001', '2025-04-01 08:00:00', 100, 9000.00),
('PK002', 'B0001', '2025-04-03 10:30:00', 100, 8900.00);

-- --------------------------------------------------------

--
-- Struktur dari tabel `detail_penjualan`
--

DROP TABLE IF EXISTS `detail_penjualan`;
CREATE TABLE IF NOT EXISTS `detail_penjualan` (
  `ID_BARANG` varchar(5) NOT NULL,
  `ID_PENJUALAN` varchar(5) NOT NULL,
  `Jumlah_Terjual` int DEFAULT NULL,
  `Subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ID_BARANG`,`ID_PENJUALAN`),
  KEY `ID_PENJUALAN` (`ID_PENJUALAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `detail_penjualan`
--

INSERT INTO `detail_penjualan` (`ID_BARANG`, `ID_PENJUALAN`, `Jumlah_Terjual`, `Subtotal`) VALUES
('B0001', 'PN001', 20, 184000.00),
('B0001', 'PN002', 30, 276000.00),
('B0002', 'PN001', 40, 272000.00),
('B0002', 'PN002', 60, 408000.00);

-- --------------------------------------------------------

--
-- Struktur dari tabel `gudang`
--

DROP TABLE IF EXISTS `gudang`;
CREATE TABLE IF NOT EXISTS `gudang` (
  `ID_GUDANG` varchar(5) NOT NULL,
  `Kapasitas` float DEFAULT NULL,
  `Satuan_Kapasitas` varchar(20) DEFAULT 'm³',
  `Alamat` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_GUDANG`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `gudang`
--

INSERT INTO `gudang` (`ID_GUDANG`, `Kapasitas`, `Satuan_Kapasitas`, `Alamat`) VALUES
('G0001', 1000, 'm³', 'Jl. Raya No. 123, Purwokerto'),
('G0002', 200.5, 'm³', 'Jl. Merdeka No. 789, Purwokerto');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kiriman`
--

DROP TABLE IF EXISTS `kiriman`;
CREATE TABLE IF NOT EXISTS `kiriman` (
  `ID_PELANGGAN_GROSIR` varchar(5) NOT NULL,
  `ID_PENGIRIMAN` varchar(5) NOT NULL,
  PRIMARY KEY (`ID_PELANGGAN_GROSIR`,`ID_PENGIRIMAN`),
  KEY `ID_PENGIRIMAN` (`ID_PENGIRIMAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `kiriman`
--

INSERT INTO `kiriman` (`ID_PELANGGAN_GROSIR`, `ID_PENGIRIMAN`) VALUES
('PR001', 'PM001'),
('PR002', 'PM001');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pegawai`
--

DROP TABLE IF EXISTS `pegawai`;
CREATE TABLE IF NOT EXISTS `pegawai` (
  `ID_PEGAWAI` varchar(5) NOT NULL,
  `ID_PEKERJAAN` varchar(5) DEFAULT NULL,
  `Nama_Pegawai` varchar(100) DEFAULT NULL,
  `Kontak_Pegawai` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_PEGAWAI`),
  KEY `ID_PEKERJAAN` (`ID_PEKERJAAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pegawai`
--

INSERT INTO `pegawai` (`ID_PEGAWAI`, `ID_PEKERJAAN`, `Nama_Pegawai`, `Kontak_Pegawai`) VALUES
('PW001', 'PJ001', 'Rahmat Budiman', '85678907856'),
('PW002', 'PJ001', 'Sarah Kasih', '87845246789'),
('PW003', 'PJ002', 'Ahmad Budi', '8668952468789');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pekerjaan`
--

DROP TABLE IF EXISTS `pekerjaan`;
CREATE TABLE IF NOT EXISTS `pekerjaan` (
  `ID_PEKERJAAN` varchar(5) NOT NULL,
  `Posisi` varchar(100) DEFAULT NULL,
  `Gaji` int DEFAULT NULL,
  PRIMARY KEY (`ID_PEKERJAAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pekerjaan`
--

INSERT INTO `pekerjaan` (`ID_PEKERJAAN`, `Posisi`, `Gaji`) VALUES
('PJ001', 'Kurir', 3500000),
('PJ002', 'Jaga Toko', 4000000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelanggan_grosir`
--

DROP TABLE IF EXISTS `pelanggan_grosir`;
CREATE TABLE IF NOT EXISTS `pelanggan_grosir` (
  `ID_PELANGGAN_GROSIR` varchar(5) NOT NULL,
  `Nama` varchar(100) DEFAULT NULL,
  `Kontak` varchar(15) DEFAULT NULL,
  `Alamat_Jalan` varchar(100) DEFAULT NULL,
  `Alamat_Kecamatan` varchar(100) DEFAULT NULL,
  `Alamat_Kabupaten` varchar(100) DEFAULT NULL,
  `Alamat_Provinsi` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_PELANGGAN_GROSIR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pelanggan_grosir`
--

INSERT INTO `pelanggan_grosir` (`ID_PELANGGAN_GROSIR`, `Nama`, `Kontak`, `Alamat_Jalan`, `Alamat_Kecamatan`, `Alamat_Kabupaten`, `Alamat_Provinsi`) VALUES
('PR001', 'Toko Kue Seberang', '87943561267', 'Jl. Dr. Angka No. 12', 'Purwokerto Barat', 'Banyumas', 'Jawa Tengah'),
('PR002', 'Toko Abudi', '84455229813', 'Jl. HR Bunyamin No. 25', 'Karangwangkal', 'Banyumas', 'Jawa Tengah');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pemasok`
--

DROP TABLE IF EXISTS `pemasok`;
CREATE TABLE IF NOT EXISTS `pemasok` (
  `ID_PEMASOK` varchar(5) NOT NULL,
  `Nama_Pemasok` varchar(100) DEFAULT NULL,
  `Alamat_Pemasok` varchar(255) DEFAULT NULL,
  `Kontak_Pemasok` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_PEMASOK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pemasok`
--

INSERT INTO `pemasok` (`ID_PEMASOK`, `Nama_Pemasok`, `Alamat_Pemasok`, `Kontak_Pemasok`) VALUES
('PK001', 'Bintang Baking Supply ', 'Jl. HR Bunyamin No. 22, Pwt Utara', '87656789076'),
('PK002', 'Mitra Kue Sejahtera', 'Jl. Raya Coklat No. 45, Purwokerto', '89034578989');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengantaran`
--

DROP TABLE IF EXISTS `pengantaran`;
CREATE TABLE IF NOT EXISTS `pengantaran` (
  `ID_PENGIRIMAN` varchar(5) NOT NULL,
  `ID_PEGAWAI` varchar(5) NOT NULL,
  PRIMARY KEY (`ID_PENGIRIMAN`,`ID_PEGAWAI`),
  KEY `ID_PEGAWAI` (`ID_PEGAWAI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pengantaran`
--

INSERT INTO `pengantaran` (`ID_PENGIRIMAN`, `ID_PEGAWAI`) VALUES
('PM001', 'PW001'),
('PM001', 'PW002');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengeluaran`
--

DROP TABLE IF EXISTS `pengeluaran`;
CREATE TABLE IF NOT EXISTS `pengeluaran` (
  `ID_PENGELUARAN` varchar(5) NOT NULL,
  `ID_PEMASOK` varchar(5) DEFAULT NULL,
  `ID_PEGAWAI` varchar(5) DEFAULT NULL,
  `Nama_Pengeluaran` varchar(100) DEFAULT NULL,
  `Jumlah_Pengeluaran` int DEFAULT NULL,
  `Tanggal_Pengeluaran` date DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_PENGELUARAN`),
  KEY `ID_PEMASOK` (`ID_PEMASOK`),
  KEY `ID_PEGAWAI` (`ID_PEGAWAI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pengeluaran`
--

INSERT INTO `pengeluaran` (`ID_PENGELUARAN`, `ID_PEMASOK`, `ID_PEGAWAI`, `Nama_Pengeluaran`, `Jumlah_Pengeluaran`, `Tanggal_Pengeluaran`) VALUES
('PG001', 'PK001', NULL, 'Pembelian Tepung dari Mitra Kue Sejahtera', 900000, '2025-04-02'),
('PG002', NULL, 'PW001', 'Gaji Rahmat bulan April', 3500000, '2025-04-05');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengiriman`
--

DROP TABLE IF EXISTS `pengiriman`;
CREATE TABLE IF NOT EXISTS `pengiriman` (
  `ID_PENGIRIMAN` varchar(5) NOT NULL,
  `Tanggal` date DEFAULT CURRENT_TIMESTAMP,
  `Status_Pengiriman` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_PENGIRIMAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pengiriman`
--

INSERT INTO `pengiriman` (`ID_PENGIRIMAN`, `Tanggal`, `Status_Pengiriman`) VALUES
('PM001', '2025-04-28', 'Dalam Perjalanan'),
('PM002', '2025-04-28', 'Menunggu Pengiriman');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penjualan`
--

DROP TABLE IF EXISTS `penjualan`;
CREATE TABLE IF NOT EXISTS `penjualan` (
  `ID_PENJUALAN` varchar(5) NOT NULL,
  `ID_PELANGGAN_GROSIR` varchar(5) DEFAULT NULL,
  `Total_Penjualan` int DEFAULT NULL,
  `Tanggal` date DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_PENJUALAN`),
  KEY `ID_PELANGGAN_GROSIR` (`ID_PELANGGAN_GROSIR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `penjualan`
--

INSERT INTO `penjualan` (`ID_PENJUALAN`, `ID_PELANGGAN_GROSIR`, `Total_Penjualan`, `Tanggal`) VALUES
('PN001', 'PR001', 456000, '2025-04-27'),
('PN002', 'PR001', 684000, '2025-04-28');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penyimpanan`
--

DROP TABLE IF EXISTS `penyimpanan`;
CREATE TABLE IF NOT EXISTS `penyimpanan` (
  `ID_BARANG` varchar(5) NOT NULL,
  `ID_GUDANG` varchar(5) NOT NULL,
  `Tanggal_masuk` date DEFAULT CURRENT_TIMESTAMP,
  `Jumlah_disimpan` int DEFAULT NULL,
  PRIMARY KEY (`ID_BARANG`,`ID_GUDANG`),
  KEY `ID_GUDANG` (`ID_GUDANG`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `penyimpanan`
--

INSERT INTO `penyimpanan` (`ID_BARANG`, `ID_GUDANG`, `Tanggal_masuk`, `Jumlah_disimpan`) VALUES
('B0001', 'G0001', '2025-04-15', 100),
('B0002', 'G0001', '2025-04-15', 100);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pesanan`
--

DROP TABLE IF EXISTS `pesanan`;
CREATE TABLE IF NOT EXISTS `pesanan` (
  `ID_PENJUALAN` varchar(5) NOT NULL,
  `ID_PENGIRIMAN` varchar(5) NOT NULL,
  PRIMARY KEY (`ID_PENJUALAN`,`ID_PENGIRIMAN`),
  KEY `ID_PENGIRIMAN` (`ID_PENGIRIMAN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pesanan`
--

INSERT INTO `pesanan` (`ID_PENJUALAN`, `ID_PENGIRIMAN`) VALUES
('PN001', 'PM001'),
('PN002', 'PM001');

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `detail_pemasokan`
--
ALTER TABLE `detail_pemasokan`
  ADD CONSTRAINT `detail_pemasokan_ibfk_1` FOREIGN KEY (`ID_BARANG`) REFERENCES `barang` (`ID_BARANG`),
  ADD CONSTRAINT `detail_pemasokan_ibfk_2` FOREIGN KEY (`ID_PEMASOK`) REFERENCES `pemasok` (`ID_PEMASOK`);

--
-- Ketidakleluasaan untuk tabel `detail_penjualan`
--
ALTER TABLE `detail_penjualan`
  ADD CONSTRAINT `detail_penjualan_ibfk_1` FOREIGN KEY (`ID_BARANG`) REFERENCES `barang` (`ID_BARANG`),
  ADD CONSTRAINT `detail_penjualan_ibfk_2` FOREIGN KEY (`ID_PENJUALAN`) REFERENCES `penjualan` (`ID_PENJUALAN`);

--
-- Ketidakleluasaan untuk tabel `kiriman`
--
ALTER TABLE `kiriman`
  ADD CONSTRAINT `kiriman_ibfk_1` FOREIGN KEY (`ID_PELANGGAN_GROSIR`) REFERENCES `pelanggan_grosir` (`ID_PELANGGAN_GROSIR`),
  ADD CONSTRAINT `kiriman_ibfk_2` FOREIGN KEY (`ID_PENGIRIMAN`) REFERENCES `pengiriman` (`ID_PENGIRIMAN`);

--
-- Ketidakleluasaan untuk tabel `pegawai`
--
ALTER TABLE `pegawai`
  ADD CONSTRAINT `pegawai_ibfk_1` FOREIGN KEY (`ID_PEKERJAAN`) REFERENCES `pekerjaan` (`ID_PEKERJAAN`);

--
-- Ketidakleluasaan untuk tabel `pengantaran`
--
ALTER TABLE `pengantaran`
  ADD CONSTRAINT `pengantaran_ibfk_1` FOREIGN KEY (`ID_PENGIRIMAN`) REFERENCES `pengiriman` (`ID_PENGIRIMAN`),
  ADD CONSTRAINT `pengantaran_ibfk_2` FOREIGN KEY (`ID_PEGAWAI`) REFERENCES `pegawai` (`ID_PEGAWAI`);

--
-- Ketidakleluasaan untuk tabel `pengeluaran`
--
ALTER TABLE `pengeluaran`
  ADD CONSTRAINT `pengeluaran_ibfk_1` FOREIGN KEY (`ID_PEMASOK`) REFERENCES `pemasok` (`ID_PEMASOK`),
  ADD CONSTRAINT `pengeluaran_ibfk_2` FOREIGN KEY (`ID_PEGAWAI`) REFERENCES `pegawai` (`ID_PEGAWAI`);

--
-- Ketidakleluasaan untuk tabel `penjualan`
--
ALTER TABLE `penjualan`
  ADD CONSTRAINT `penjualan_ibfk_1` FOREIGN KEY (`ID_PELANGGAN_GROSIR`) REFERENCES `pelanggan_grosir` (`ID_PELANGGAN_GROSIR`);

--
-- Ketidakleluasaan untuk tabel `penyimpanan`
--
ALTER TABLE `penyimpanan`
  ADD CONSTRAINT `penyimpanan_ibfk_1` FOREIGN KEY (`ID_BARANG`) REFERENCES `barang` (`ID_BARANG`),
  ADD CONSTRAINT `penyimpanan_ibfk_2` FOREIGN KEY (`ID_GUDANG`) REFERENCES `gudang` (`ID_GUDANG`);

--
-- Ketidakleluasaan untuk tabel `pesanan`
--
ALTER TABLE `pesanan`
  ADD CONSTRAINT `pesanan_ibfk_1` FOREIGN KEY (`ID_PENJUALAN`) REFERENCES `penjualan` (`ID_PENJUALAN`),
  ADD CONSTRAINT `pesanan_ibfk_2` FOREIGN KEY (`ID_PENGIRIMAN`) REFERENCES `pengiriman` (`ID_PENGIRIMAN`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
