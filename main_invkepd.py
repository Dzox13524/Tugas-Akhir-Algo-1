from inv_d import inventaris_daerah
from histori_lp import histori_laporan

def menu_inventaris(daerah):
        while True:
            teks = "Menu Inventaris Daerah"
            print("\n╔═══════════════════════════════════════════════════════╗")
            print(f"║{teks:^55}║")
            print("╠═══════════════════════════════════════════════════════╣")
            men = {
                '1': 'Data Inventaris Daerah',
                '2': 'Histori Laporan',
                '3': 'Keluar'
            }
            keys = list(men.keys())
            values = list(men.values())

            for key, value in zip(keys, values):
                print(f"║ {key:<1} . {value:<49} ║")
            print("╚═══════════════════════════════════════════════════════╝")

            try:
                pilihan = int(input("Pilih menu [1-3]: ").strip())
                if pilihan == 1:
                    inventaris_daerah(daerah)
                elif pilihan == 2:
                    histori_laporan(daerah)
                elif pilihan == 3:
                    teks = "Keluar dari Menu Inventaris."
                    print("\n╔════════════════════════════════════════════════════════╗")
                    print(f"║{teks:^56}║")
                    print("╚════════════════════════════════════════════════════════╝")
                    break
                else:
                    print("Pilihan tidak valid. Masukkan angka antara 1-3.")
            except ValueError:
                print("Input harus berupa angka.")