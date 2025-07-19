# Daftar menu dalam list tuple (nama menu, harga)
daftar_menu = [
    ("Nasi Goreng", 25000),
    ("Ayam Bakar", 30000),
    ("Mie Goreng", 20000),
    ("Sate Ayam", 35000),
    ("Es Teh Manis", 5000)
]

# Fungsi menampilkan menu
def tampilkan_menu():
    print("Menu Restoran:")
    for i, (nama, harga) in enumerate(daftar_menu, start=1):
        print(f"{i}. {nama} - Rp{harga}")

# Fungsi menghitung subtotal
def hitung_total(harga, jumlah):
    return harga * jumlah

# Fungsi menghitung diskon
def hitung_diskon(total):
    if total > 200000:
        return total * 0.1
    else:
        return 0

# Program utama
def main():
    tampilkan_menu()
    total_semua = 0
    keranjang = []  # List untuk menyimpan detail pesanan

    while True:
        pilihan = int(input("\nMasukkan nomor menu yang ingin dipesan (0 untuk selesai): "))

        if pilihan == 0:
            break

        if pilihan < 1 or pilihan > len(daftar_menu):
            print("Nomor menu tidak valid.")
            continue

        jumlah = int(input("Masukkan jumlah porsi: "))
        nama_menu, harga_satuan = daftar_menu[pilihan - 1]
        subtotal = hitung_total(harga_satuan, jumlah)
        total_semua += subtotal

        keranjang.append((nama_menu, jumlah, harga_satuan, subtotal))

    if not keranjang:
        print("\nTidak ada pesanan.")
        return

    diskon = hitung_diskon(total_semua)
    total_bayar = total_semua - diskon

    # Cetak struk
    print("\n===== STRUK PEMBAYARAN =====")
    for item in keranjang:
        nama, jumlah, harga, subtotal = item
        print(f"- {nama} x{jumlah} @Rp{harga} = Rp{subtotal}")
    print(f"\nTotal Harga : Rp{total_semua}")
    print(f"Diskon      : Rp{diskon}")

    if diskon > 0:
        print("Keterangan  : Dapat Diskon 10%")
    else:
        print("Keterangan  : Tidak Dapat Diskon")

    print(f"Total Bayar : Rp{total_bayar}")

# Jalankan program
main()
