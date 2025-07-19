# Daftar buku dalam list tuple (judul, harga)
daftar_buku = [
    ("Python Dasar", 50000),
    ("Belajar AI", 80000),
    ("Pemrograman Web", 70000)
]

# Fungsi untuk menampilkan daftar buku
def tampilkan_buku():
    print("Daftar Buku:")
    for i, (judul, harga) in enumerate(daftar_buku, start=1):
        print(f"{i}. {judul} - Rp{harga}")

# Fungsi menghitung total harga
def hitung_total(harga, jumlah):
    return harga * jumlah

# Fungsi menghitung diskon
def hitung_diskon(total):
    if total > 150000:
        return total * 0.1
    else:
        return 0

# Program utama
def main():
    tampilkan_buku()
    pilihan = int(input("Masukkan nomor buku yang ingin dibeli: "))

    if pilihan < 1 or pilihan > len(daftar_buku):
        print("Nomor buku tidak valid.")
        return

    jumlah = int(input("Masukkan jumlah buku: "))
    judul, harga_satuan = daftar_buku[pilihan - 1]
    total = hitung_total(harga_satuan, jumlah)
    diskon = hitung_diskon(total)
    total_bayar = total - diskon

    print("\n===== STRUK PEMBELIAN =====")
    print(f"Buku         : {judul}")
    print(f"Jumlah       : {jumlah}")
    print(f"Harga Satuan : Rp{harga_satuan}")
    print(f"Total Harga  : Rp{total}")
    print(f"Diskon       : Rp{diskon}")

    if diskon > 0:
        print("Keterangan   : Dapat Diskon 10%")
    else:
        print("Keterangan   : Tidak Dapat Diskon")

    print(f"Total Bayar  : Rp{total_bayar}")

# Jalankan program
main()
