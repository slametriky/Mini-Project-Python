# Fungsi menentukan tarif per jam
def tarif_per_jam(jenis):
    if jenis == "motor":
        return 2000
    elif jenis == "mobil":
        return 5000
    else:
        return 0

# Fungsi hitung total biaya
def hitung_biaya(tarif, lama):
    return tarif * lama

# Fungsi hitung diskon
def hitung_diskon(total, lama):
    if lama > 5:
        return total * 0.1
    else:
        return 0

# Program utama
def main():
    jenis = input("Masukkan jenis kendaraan (motor/mobil): ").lower()
    tarif = tarif_per_jam(jenis)

    if tarif == 0:
        print("Jenis kendaraan tidak valid.")
        return

    lama = int(input("Masukkan lama parkir (jam): "))
    total = hitung_biaya(tarif, lama)
    diskon = hitung_diskon(total, lama)
    total_bayar = total - diskon

    print("\n===== STRUK PARKIR =====")
    print(f"Jenis Kendaraan : {jenis}")
    print(f"Lama Parkir     : {lama} jam")
    print(f"Tarif per Jam   : Rp{tarif}")
    print(f"Total Biaya     : Rp{total}")
    print(f"Diskon          : Rp{diskon}")

    if diskon > 0:
        print("Keterangan      : Dapat Diskon 10%")
    else:
        print("Keterangan      : Tidak Dapat Diskon")

    print(f"Total Bayar     : Rp{total_bayar}")

# Jalankan program
main()
