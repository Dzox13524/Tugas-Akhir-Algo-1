import csv

def inventaris_daerah(daerah):
    try:
        inventaris = {} 

        with open("laporan.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Daerah"] == daerah and row["status"] == "acc":
                    jenis_barang = row["Jenis Barang"].split(";")
                    jumlah_barang = row["Jumlah Barang"].split(";")
                    for i in range(len(jenis_barang)):
                        barang = jenis_barang[i]
                        jumlah = int(jumlah_barang[i])
                        if barang in inventaris:
                            inventaris[barang] += jumlah
                        else:
                            inventaris[barang] = jumlah  
        
        if inventaris:
            teks = f"Inventaris Daerah {daerah}"
            print("\n╔═══════════════════════════════════════════════════════╗")
            print(f"║{teks:^55}║")
            print("╠═══════════════════════════════════════════════════════╣")
            print("║ Barang                          | Jumlah              ║")
            print("╠═══════════════════════════════════════════════════════╣")

            for barang in inventaris:
                jumlah = inventaris[barang]
                l_barang = 31 - len(barang) 
                l_jumlah = 19 - len(str(jumlah)) 

                baris = "║ " + barang + (" " * l_barang) + " | " + (" " * l_jumlah) + str(jumlah) + " ║"
                print(baris)

            print("╚═══════════════════════════════════════════════════════╝")
        else:
            print(f"\nTidak ada data inventaris untuk daerah {daerah}.")

    except FileNotFoundError:
        print("Error: File laporan.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")