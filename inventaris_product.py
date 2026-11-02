
class InventarisProduk:
    def __init__(self):
        # Hash Table untuk menyimpan data produk
        # Key = ID Produk, Value = detail produk
        self.data_produk = {}

    # 1. Method untuk menambahkan produk
    def tambah_produk(self, id_produk, nama, harga, stok):
        if id_produk in self.data_produk:
            print("\nID produk sudah terdaftar!")
            return

        self.data_produk[id_produk] = {
            "nama": nama,
            "harga": harga,
            "stok": stok
        }

        print("\nProduk berhasil ditambahkan!")

    # 2. Method untuk mencari produk berdasarkan ID
    def cari_produk(self, id_produk):
        if id_produk in self.data_produk:
            produk = self.data_produk[id_produk]

            print("\n=== DETAIL PRODUK ===")
            print("ID Produk  :", id_produk)
            print("Nama Produk:", produk["nama"])
            print("Harga      : Rp", produk["harga"])
            print("Stok       :", produk["stok"])
        else:
            print("\nProduk tidak ditemukan!")

    # 3. Method untuk menghapus produk berdasarkan ID
    def hapus_produk(self, id_produk):
        if id_produk in self.data_produk:
            del self.data_produk[id_produk]
            print("\nProduk berhasil dihapus!")
        else:
            print("\nProduk tidak ditemukan!")

    # 4. Method untuk menampilkan semua produk
    def tampilkan_produk(self):
        if not self.data_produk:
            print("\nInventaris masih kosong!")
            return

        print("\n=== DAFTAR INVENTARIS PRODUK ===")

        for id_produk, produk in self.data_produk.items():
            print("------------------------------")
            print("ID Produk  :", id_produk)
            print("Nama Produk:", produk["nama"])
            print("Harga      : Rp", produk["harga"])
            print("Stok       :", produk["stok"])

        print("------------------------------")


# Program utama (Command Line Interface)
def main():
    inventaris = InventarisProduk()

    while True:
        print("\n================================")
        print(" SISTEM MANAJEMEN INVENTARIS")
        print("================================")
        print("1. Tambah Produk")
        print("2. Cari Produk")
        print("3. Hapus Produk")
        print("4. Tampilkan Semua Produk")
        print("5. Keluar")
        print("================================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("\n=== TAMBAH PRODUK ===")

            id_produk = input("Masukkan ID Produk: ").strip()
            nama = input("Masukkan Nama Produk: ").strip()

            try:
                harga = float(input("Masukkan Harga Produk: "))
                stok = int(input("Masukkan Jumlah Stok: "))

                if not id_produk or not nama:
                    print("\nID dan nama produk tidak boleh kosong!")
                elif harga < 0 or stok < 0:
                    print("\nHarga dan stok tidak boleh negatif!")
                else:
                    inventaris.tambah_produk(
                        id_produk, nama, harga, stok
                    )

            except ValueError:
                print("\nInput salah! Harga harus angka dan stok harus bilangan bulat.")

        elif pilihan == "2":
            print("\n=== CARI PRODUK ===")
            id_produk = input("Masukkan ID Produk: ").strip()
            inventaris.cari_produk(id_produk)

        elif pilihan == "3":
            print("\n=== HAPUS PRODUK ===")
            id_produk = input("Masukkan ID Produk: ").strip()
            inventaris.hapus_produk(id_produk)

        elif pilihan == "4":
            inventaris.tampilkan_produk()

        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan program.")
            break

        else:
            print("\nPilihan tidak valid! Silakan pilih menu 1-5.")


if __name__ == "__main__":
    main()
