def tampilkan_menu_minuman(daftar_menu, daftar_jumlah, daftar_harga, daftar_total_harga):
    """
    Menampilkan menu minuman dan mencatat pesanan.
    """
    print("\n+=======================================+")
    print("| MINUMAN\t\t| HARGA\t\t|")
    print("+=======================================+")
    print("| DINGIN ❄️\t\t\t\t |")
    print("+---------------------------------------+")
    print("| [1] Lemon Tea\t\t| Rp10.000\t|")
    print("| [2] Ice Coffee \t| Rp15.000\t|")
    print("| [3] Ice Chocolate\t| Rp15.000\t|")
    print("+---------------------------------------+")
    print("| HANGAT ♨️\t\t\t\t |")
    print("+---------------------------------------+")
    print("| [4] Hot Tea\t\t| Rp15.000\t|")
    print("| [5] Hot Coffee\t| Rp12.000\t|")
    print("| [6] Hot Chocolate\t| Rp20.000\t|")
    print("+=======================================+")
    jumlah_jenis_minuman = int(input("Masukkan jumlah jenis minuman yang ingin Anda pesan: "))
    for angka in range(jumlah_jenis_minuman):
        print(f"\nJenis ke-{angka+1}")
        pilihan_minuman = int(input("Masukkan nomor pilihan minuman (1/2/3/4/5/6): "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan untuk pilihan ini: "))
        daftar_jumlah.append(jumlah_pesanan)
        if pilihan_minuman == 1:
            daftar_menu.append("Lemon Tea")
            daftar_harga.append(10000)
            daftar_total_harga.append(jumlah_pesanan * 10000)
        elif pilihan_minuman == 2:
            daftar_menu.append("Ice Coffee")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan * 15000)
        elif pilihan_minuman == 3:
            daftar_menu.append("Ice Chocolate")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan * 15000)
        elif pilihan_minuman == 4:
            daftar_menu.append("Hot Tea")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan * 15000)
        elif pilihan_minuman == 5:
            daftar_menu.append("Hot Coffee")
            daftar_harga.append(12000)
            daftar_total_harga.append(jumlah_pesanan * 12000)
        elif pilihan_minuman == 6:
            daftar_menu.append("Hot Chocolate")
            daftar_harga.append(20000)
            daftar_total_harga.append(jumlah_pesanan * 20000)
        else:
            print("\nPilihan minuman tidak valid. Silakan pilih antara 1-6.")
