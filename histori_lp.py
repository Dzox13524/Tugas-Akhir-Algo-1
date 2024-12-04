import pandas as pd

def histori_laporan(daerah):
    try:
        data = pd.read_csv('laporan.csv')
        data2 = data[data['Daerah'] == daerah]
        if len(data2) == 0:
            return print("\nTidak ada histori laporan untuk daerah Anda.")
        data_terakhir = data2.iloc[-1]
        data_l = {
                "Tanggal": data_terakhir['Tanggal'],
                "Daerah": data_terakhir['Daerah'],
                "Jenis Barang": data_terakhir['Jenis Barang'],
                "Jumlah Barang": data_terakhir['Jumlah Barang'],
                "Alasan": data_terakhir['Alasan'],
                "status": data_terakhir['status'],
                "respon": data_terakhir['respon'],
            }

        keys = data_l
        values = [data_l[key] for key in keys]

        print("\n╔═══════════════════════════════════════════════════════╗")
        print(f"║ {'Histori Laporan Terakhir':^53} ║")
        print("╠═══════════════════════════════════════════════════════╣")

        lebar_key = 15
        lebar_val = 35

        for key, value in zip(keys, values):
            value = str(value) 
            value_lines = [value[i:i+lebar_val] for i in range(0, len(value), lebar_val)]

            print(f"║ {key:<{lebar_key}} : {value_lines[0]:<{lebar_val}} ║")

        for line in value_lines[1:]:
            print(f"║ {'':<{lebar_key}}   {line:<{lebar_val}} ║")

            break
        print("╚═══════════════════════════════════════════════════════╝")

    except FileNotFoundError:
        print("Error: File laporan.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        