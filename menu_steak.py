def tampilkan_menu_steak(daftar_menu, daftar_jumlah, daftar_harga, daftar_total_harga):
    """
    Menampilkan menu steak dan mencatat pesanan pengguna.
    """
    print("\n===================================")
    print("JENIS STEAK\t\t| HARGA")
    print("===================================")
    print("1. Ribeye\t\t| Rp150.000")
    print("2. Sirloin\t\t| Rp130.000")
    print("3. Tenderloin\t\t| Rp180.000")
    print("4. T-Bone\t\t| Rp170.000")
    print("5. Wagyu Striploin\t| Rp300.000")
    jumlah_jenis_steak = int(input("\nMasukkan jumlah jenis steak yang ingin Anda pesan: "))
    for nomor in range(jumlah_jenis_steak):
        print(f"\nJenis Ke-{nomor + 1}")
        pilihan_steak = int(input("Masukkan nomor pilihan steak (1/2/3/4/5): "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan untuk pilihan ini: "))
        daftar_jumlah.append(jumlah_pesanan)
        if pilihan_steak == 1:
            daftar_menu.append("Ribeye")
            daftar_harga.append(150000)
            daftar_total_harga.append(jumlah_pesanan * 150000)
        elif pilihan_steak == 2:
            daftar_menu.append("Sirloin")
            daftar_harga.append(130000)
            daftar_total_harga.append(jumlah_pesanan * 130000)
        elif pilihan_steak == 3:
            daftar_menu.append("Tenderloin")
            daftar_harga.append(180000)
            daftar_total_harga.append(jumlah_pesanan * 180000)
        elif pilihan_steak == 4:
            daftar_menu.append("T-Bone")
            daftar_harga.append(170000)
            daftar_total_harga.append(jumlah_pesanan * 170000)
        elif pilihan_steak == 5:
            daftar_menu.append("Wagyu Striploin")
            daftar_harga.append(300000)
            daftar_total_harga.append(jumlah_pesanan * 300000)
        else:
            print("\nPilihan steak tidak valid. Silakan pilih antara 1-5.")