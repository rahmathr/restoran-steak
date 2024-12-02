import pandas as pd
import menu_steak,menu_minuman
daftar_menu = []
daftar_jumlah = []
daftar_harga = []
daftar_total_harga = []
while True:
    print("\n+===============================+")
    print("|\tRESTORAN STEAK 🥩\t|")
    print("+===============================+")
    print("| [1] Lihat Menu\t\t|")
    print("| [2] Pesanan Anda\t\t|")
    print("| [3] Exit\t\t\t|")
    print("+===============================+")
    pilihan_opsi = int(input("Pilih opsi (1/2/3): "))
    if pilihan_opsi == 1:
        print("\n+=======================+")
        print("|\tMENU 📃\t\t|")
        print("+=======================+")
        print("| [1] Steak\t\t|")
        print("| [2] Minuman\t\t|")
        print("+=======================+")
        pilihan_menu = int(input("Pilih menu (1/2): "))
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
        print("\n+=======================================================+")
        print("|\t\t\tPESANAN ANDA\t\t\t|")
        print("+=======================================================+")
        print(tabel_data)
        print("=========================================================")
        # Hitung Total Bayar sebelum dikenakan ppn
        total = 0
        for total_bayar in daftar_total_harga:
            total += total_bayar
        print(f"Total Harga\t   = Rp{total}")
        # Hitung ppn
        pajak = total*(12/100)
        print(f"PPN 12%\t\t   = Rp{int(pajak)}")
        # Hitung total keseluruhan
        total_bayar = total + pajak
        print(f"Total Bayar\t   = Rp{int(total_bayar)}")
        print()
        # Hitung uang pelanggan
        uang_pelanggan = int(input("masukkan uang anda = Rp"))
        kembalian = uang_pelanggan - total_bayar
        print(f"total kembalian\t   = Rp{int(kembalian)}")
        break
    elif pilihan_opsi == 3:
        print("\nSelamat datang kembali 🙏")
        break
    else:
        print("\nOpsi tidak valid. Silakan pilih 1 untuk MENU atau 2 untuk PESANAN ANDA.")
