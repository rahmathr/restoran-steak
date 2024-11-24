import pandas as pd

def tampilkan_menu_steak():
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
    for index in range(jumlah_jenis_steak):
        print(f"\nJenis Ke-{index + 1}")
        pilihan_steak = int(input("Masukkan nomor pilihan steak (1/2/3/4/5): "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan untuk pilihan ini: "))
        daftar_jumlah.append(jumlah_pesanan)
        if pilihan_steak == 1:
            daftar_menu.append("Ribeye")
            daftar_harga.append(150000)
            daftar_total_harga.append(jumlah_pesanan*150000)
        elif pilihan_steak == 2:
            daftar_menu.append("Sirloin")
            daftar_harga.append(130000)
            daftar_total_harga.append(jumlah_pesanan*130000)
        elif pilihan_steak == 3:
            daftar_menu.append("Tenderloin")
            daftar_harga.append(180000)
            daftar_total_harga.append(jumlah_pesanan*180000)
        elif pilihan_steak == 4:
            daftar_menu.append("T-Bone")
            daftar_harga.append(170000)
            daftar_total_harga.append(jumlah_pesanan*170000)
        elif pilihan_steak == 5:
            daftar_menu.append("Wagyu Striploin")
            daftar_harga.append(300000)
            daftar_total_harga.append(jumlah_pesanan*300000)
        else:
            print("Pilihan steak tidak valid. Silakan pilih antara 1-5.")

def tampilkan_menu_pendamping():
    """
    Menampilkan menu makanan pendamping dan mencatat pesanan.
    """
    print("\n===================================")
    print("MAKANAN PENDAMPING\t| HARGA")
    print("===================================")
    print("1. Mashed Potato\t| Rp20.000")
    print("2. French Fries \t| Rp15.000")
    print("3. Sauteed Vegetables   | Rp15.000")
    jumlah_makanan_pendamping = int(input("\nMasukkan jumlah jenis makanan pendamping yang ingin Anda pesan: "))
    for i in range(jumlah_makanan_pendamping):
        print(f"\nJenis ke-{i+1}")
        jumlah_makanan_pendamping = int(input("Masukkan nomor pilihan makanan pendamping (1/2/3): "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan untuk pilihan ini: "))
        daftar_jumlah.append(jumlah_pesanan)
        if jumlah_makanan_pendamping == 1:
            daftar_menu.append("Mashed Potato")
            daftar_harga.append(20000)
            daftar_total_harga.append(jumlah_pesanan*20000)
        elif jumlah_makanan_pendamping == 2:
            daftar_menu.append("French Fries")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan*15000)
        elif jumlah_makanan_pendamping == 3:
            daftar_menu.append("Sauteed Vegetables")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan*15000)
        else:
            print("Pilihan makanan pendamping tidak valid. Silakan pilih antara 1-3.")

def tampilkan_menu_saus():
    """
    Menampilkan menu saus dan mencatat pesanan.
    """
    print("\n===================================")
    print("SAUS\t| HARGA")
    print("===================================")
    print("1. Mushroom Sauce\t| Rp10.000")
    print("2. Blackpepper Sauce\t| Rp10.000")
    print("3. BBQ Sauce\t\t| Rp10.000")
    jumlah_jenis_saus = int(input("\nMasukkan jumlah jenis saus yang ingin Anda pesan: "))
    for i in range(jumlah_jenis_saus):
        print(f"\nJenis ke-{i+1}")
        jumlah_jenis_saus = int(input("Masukkan nomor pilihan saus (1/2/3): "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan untuk pilihan ini: "))
        daftar_jumlah.append(jumlah_pesanan)
        if jumlah_jenis_saus == 1:
            daftar_menu.append("Mushroom Sauce")
            daftar_harga.append(10000)
            daftar_total_harga.append(jumlah_pesanan*10000)
        elif jumlah_jenis_saus == 2:
            daftar_menu.append("Blackpepper Sauce")
            daftar_harga.append(10000)
            daftar_total_harga.append(jumlah_pesanan*10000)
        elif jumlah_jenis_saus == 3:
            daftar_menu.append("BBQ Sauce")
            daftar_harga.append(10000)
            daftar_total_harga.append(jumlah_pesanan*10000)
        else:
            print("Pilihan saus tidak valid. Silakan pilih antara 1-3.")

def tampilkan_menu_minuman():
    """
    Menampilkan menu minuman dan mencatat pesanan.
    """
    print("\n===================================")
    print("MINUMAN\t\t\t| HARGA")
    print("===================================")
    print("MINUMAN DINGIN")
    print("1. Lemon Tea\t\t| Rp10.000")
    print("2. Ice Coffee \t\t| Rp15.000")
    print("3. Ice Chocolate\t| Rp15.000")
    print("\nMINUMAN HANGAT")
    print("4. Hot Tea\t\t| Rp15.000")
    print("5. Hot Coffee\t\t| Rp12.000")
    print("6. Hot Chocolate\t| Rp20.000")
    jumlah_jenis_minuman = int(input("\nMasukkan jumlah jenis minuman yang ingin Anda pesan: "))
    for i in range(jumlah_jenis_minuman):
        print(f"\nJenis ke-{i+1}") 
        jumlah_jenis_minuman = int(input("Masukkan nomor pilihan minuman (1/2/3/4/5/6): "))
        jumlah_pesanan = int(input("Masukkan jumlah pesanan untuk pilihan ini: "))
        daftar_jumlah.append(jumlah_pesanan)
        if jumlah_jenis_minuman == 1:
            daftar_menu.append("Lemon Tea")
            daftar_harga.append(10000)
            daftar_total_harga.append(jumlah_pesanan*10000)
        elif jumlah_jenis_minuman == 2:
            daftar_menu.append("Ice Coffee")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan*15000)
        elif jumlah_jenis_minuman == 3:
            daftar_menu.append("Ice Chocolate")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan*15000)
        elif jumlah_jenis_minuman == 4:
            daftar_menu.append("Hot Tea")
            daftar_harga.append(15000)
            daftar_total_harga.append(jumlah_pesanan*15000)
        elif jumlah_jenis_minuman == 5:
            daftar_menu.append("BBQ SauceHot Coffee")
            daftar_harga.append(12000)
            daftar_total_harga.append(jumlah_pesanan*12000)
        elif jumlah_jenis_minuman == 6:
            daftar_menu.append("Hot Chocolate")
            daftar_harga.append(20000)
            daftar_total_harga.append(jumlah_pesanan*20000)
        else:
            print("Pilihan minuman tidak valid. Silakan pilih antara 1-6.")

daftar_menu = []
daftar_jumlah = []
daftar_harga = []
daftar_total_harga = []

# PROGRAM UTAMA
while True:
    print("==================================")
    print("\tRESTORAN STEAK 🥩")
    print("==================================")
    print("1. MENU")
    print("2. PESANAN ANDA")
    pilihan_opsi = int(input("\nPilih opsi (1/2): "))
    if pilihan_opsi == 1:
        print("\n=====================")
        print("\tMENU")
        print("=====================")
        print("1. Steak")
        print("2. Minuman")
        print("3. Sides")
        print("4. Saus")
        pilihan_menu = int(input("\nPilih menu (1/2/3/4): "))
        if pilihan_menu == 1:
            tampilkan_menu_steak()
        elif pilihan_menu == 2:
            tampilkan_menu_minuman()
        elif pilihan_menu == 3:
            tampilkan_menu_pendamping()
        elif pilihan_menu == 4:
            tampilkan_menu_saus()
        else:
            print("Pilihan menu tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")
    elif pilihan_opsi == 2:
        data = {
            "Nama Menu": daftar_menu,
            "Harga Satuan": daftar_harga,
            "Jumlah": daftar_jumlah,
            "Total Harga": daftar_total_harga
        }
        tabel_data = pd.DataFrame(data)
        print("\n==================== PESANAN ANDA ====================\n")
        print(tabel_data)
        print("\n======================================================")
        total = 0
        for total_bayar in daftar_total_harga:
            total += total_bayar
        print(f"JumlahBayar : Rp{total}")
        # Menghitung pajak
        pajak = total*(12/100)
        print(f"Pajak 12% : Rp{int(pajak)}")
        # Menghitung total keseluruhan
        total_bayar = total + pajak
        print(f"Total yang harus dibayar : Rp{int(total_bayar)}")
        print()
        break
    else:
        print("Opsi tidak valid. Silakan pilih 1 untuk MENU atau 2 untuk PESANAN ANDA.")
