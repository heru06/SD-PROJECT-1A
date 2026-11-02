# SD-PROJECT-A1
# Sistem Manajemen Inventaris Produk

## Deskripsi Proyek

Sistem Manajemen Inventaris Produk merupakan program berbasis Python yang dibuat untuk memenuhi tugas Proyek 1 mata kuliah yang membahas analisis kompleksitas algoritma dan struktur data.

Program ini dirancang untuk membantu pengelolaan inventaris produk pada perusahaan e-commerce, terutama dalam menangani data produk yang terus bertambah. Sistem menggunakan struktur data **Hash Table yang diimplementasikan melalui `dictionary` (`dict`) pada Python** untuk menyimpan dan mengelola data produk secara efisien.

## Tujuan Proyek

1. Menerapkan konsep Abstract Data Type (ADT) dalam pemrograman Python.
2. Menganalisis kompleksitas waktu dari operasi penyisipan, pencarian, dan penghapusan data.
3. Membandingkan struktur data Python `list`, Linked List, dan Hash Table.
4. Menentukan struktur data yang sesuai untuk pengelolaan inventaris produk berdasarkan kompleksitas algoritma.

## Fitur Program

- **Tambah Produk:** Menambahkan produk baru ke dalam inventaris.
- **Cari Produk:** Mencari detail produk berdasarkan ID Produk.
- **Hapus Produk:** Menghapus produk berdasarkan ID Produk.
- **Tampilkan Semua Produk:** Menampilkan seluruh produk yang tersimpan dalam inventaris.
- **Validasi Input:** Memeriksa input harga dan stok serta mencegah ID produk yang sama digunakan untuk produk berbeda.

## Atribut Data Produk

Setiap produk memiliki atribut berikut:

- `id_produk`: ID unik untuk setiap produk.
- `nama`: Nama produk.
- `harga`: Harga produk.
- `stok`: Jumlah stok produk yang tersedia.

## Struktur Data dan Kompleksitas

Program menggunakan Hash Table melalui Python `dict` dengan ID produk sebagai kunci (*key*) dan detail produk sebagai nilai (*value*).

Kompleksitas waktu rata-rata operasi utama:

| Operasi | Kompleksitas |
|---|---|
| Penyisipan produk | O(1) |
| Pencarian produk | O(1) |
| Penghapusan produk | O(1) |
| Menampilkan seluruh produk | O(n) |

Keterangan: `n` merupakan jumlah produk yang tersimpan. Kompleksitas O(1) untuk operasi Hash Table merupakan kompleksitas rata-rata, sedangkan kondisi terburuk dapat mencapai O(n).

## Teknologi yang Digunakan

- Bahasa pemrograman Python 3
- Struktur data Dictionary (`dict`)
- Konsep Abstract Data Type (ADT)
- Command Line Interface (CLI)

## Cara Menjalankan Program

1. Pastikan Python 3 telah terpasang pada komputer.
2. Unduh atau *clone* repositori ini.
3. Buka terminal pada folder proyek.
4. Jalankan perintah berikut:

```bash
python inventaris_produk.py
```

5. Pilih menu yang tersedia untuk menambahkan, mencari, menghapus, atau menampilkan produk.

## Kesimpulan

Penggunaan Hash Table melalui Python `dict` dipilih karena mendukung penyisipan, pencarian, dan penghapusan produk dengan kompleksitas waktu rata-rata O(1). Struktur ini sesuai untuk demonstrasi sistem inventaris yang membutuhkan akses data berdasarkan ID Produk secara efisien.

Proyek ini merupakan implementasi dasar berbasis CLI. Data disimpan di memori selama program berjalan dan belum menggunakan database permanen.

---

**Proyek 1 — Analisis Kompleksitas Algoritma dan Struktur Data**

**Studi Kasus:** Sistem Manajemen Inventaris Produk  
**Bahasa Pemrograman:** Python
