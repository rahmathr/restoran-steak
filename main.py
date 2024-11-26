import pandas as pd
import menu_steak,menu_minuman
global daftar_menu,daf,daftar_jumlah,daftar_harga,daftar_total_harga
daftar_menu = []
daftar_jumlah = []
daftar_harga = []
daftar_total_harga = []
while True:
    print("\n==================================")
    print("\tRESTORAN STEAK 🥩")
    print("==================================")
    print("1. LIHAT MENU")
    print("2. PESANAN ANDA")
    pilihan_opsi = int(input("\nPilih opsi (1/2): "))
    if pilihan_opsi == 1:
        print("\n=====================")
        print("\tMENU")
        print("=====================")
        print("1. STEAK")
        print("2. MINUMAN")
        pilihan_menu = int(input("\nPilih menu (1/2): "))
        if pilihan_menu == 1:
            menu_steak.tampilkan_menu_steak(daftar_menu,daftar_harga,daftar_jumlah,daftar_total_harga)
        elif pilihan_menu == 2:
            menu_minuman.tampilkan_menu_minuman(daftar_menu,daftar_harga,daftar_jumlah,daftar_total_harga)
        else:
            print("\nPilihan menu tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")
    elif pilihan_opsi == 2:
        data = {
            "NamaMenu": daftar_menu,
            "HargaSatuan": daftar_harga,
            "Jumlah": daftar_jumlah,
            "TotalHarga": daftar_total_harga
        }
        tabel_data = pd.DataFrame(data)
        print("\n==================== PESANAN ANDA ====================\n")
        print(tabel_data)
        print("\n======================================================")
        # Hitung Total Bayar sebelum dikenakan ppn
        total = 0
        for total_bayar in daftar_total_harga:
            total += total_bayar
        print(f"Jumlah Bayar \t\t : Rp{total}")
        # Hitung ppn
        pajak = total*(12/100)
        print(f"PPN 12%\t\t\t : Rp{int(pajak)}")
        # Hitung total keseluruhan
        total_bayar = total + pajak
        print(f"Total yang harus dibayar : Rp{int(total_bayar)}")
        print()
        break
    else:
        print("\nOpsi tidak valid. Silakan pilih 1 untuk MENU atau 2 untuk PESANAN ANDA.")
