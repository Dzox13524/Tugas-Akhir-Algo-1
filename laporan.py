import pandas as pd
from datetime import datetime

def data_csv():
    subsidi = pd.read_csv("subsidi.csv")
    subsidi = subsidi.dropna(axis=1, how='all')
    subsidi = subsidi.dropna(axis=0, how='all')
    subsidi = subsidi.fillna("")
    return subsidi

def tampilan_barang(subsidi):
    print("\n")
    print("\n╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                       LIST BARANG DAN BAHAN SUBSIDI PERTANIAN                                                                   ║")
    print("╠═══════════════════════════════╦════════════════════════════════╦═════════════════════════════════╦═══════════════════════════════╦══════════════════════════════╣")
    print("║ Benih [A]                     ║ Pupuk [B]                      ║ Pestisida [C]                   ║ Herbisida [D]                 ║ Barang [E]                   ║")
    print("╠═══════════════════════════════╬════════════════════════════════╬═════════════════════════════════╬═══════════════════════════════╬══════════════════════════════╣")

    max_rows = len(subsidi)
    for i in range(max_rows):
        benih = f"A.{i+1} {subsidi['Benih'][i]}" if subsidi['Benih'][i] else ""
        pupuk = f"B.{i+1} {subsidi['Pupuk'][i]}" if subsidi['Pupuk'][i] else ""
        pestisida = f"C.{i+1} {subsidi['Pestisida'][i]}" if subsidi['Pestisida'][i] else ""
        herbisida = f"D.{i+1} {subsidi['Herbisida'][i]}" if subsidi['Herbisida'][i] else ""
        barang = f"E.{i+1} {subsidi['Barang'][i]}" if subsidi['Barang'][i] else ""

        print(f"║ {benih:<29} ║ {pupuk:<30} ║ {pestisida:<31} ║ {herbisida:<29} ║ {barang:<28} ║")

        if i < max_rows - 1:
            print("╠═══════════════════════════════╬════════════════════════════════╬═════════════════════════════════╬═══════════════════════════════╬══════════════════════════════╣")
        else:
            print("╚═══════════════════════════════╩════════════════════════════════╩═════════════════════════════════╩═══════════════════════════════╩══════════════════════════════╝")

def Ringkasan(barang_list, jumlah_list):
    lebar_barang = 30
    lebar_jumlah = 19  
    print("╔════════════════════════════════════════════════════════╗")
    print(f"║ {'DAFTAR BARANG DAN BAHAN SUBSIDI DIPILIH':^54} ║")
    print("╠════════════════════════════════════════════════════════╣")
    for i, (barang, jumlah) in enumerate(zip(barang_list, jumlah_list), start=1):
        print(f"║ {i:<3} {barang:<{lebar_barang}} {jumlah:<{lebar_jumlah}} ║")
    print("╚════════════════════════════════════════════════════════╝")

def e_Ringkasan(barang_list, jumlah_list, subsidi):
    edit = input("\nApakah ada daftar barang yang tidak sesuai? (y/n): ").strip().lower()
    if edit == "y":
        opsi = input("\nApakah anda ingin mengubah kode barang atau menghapus barang? (ketik 'ubah'/'hapus')\nKetik pilihan: ").strip().lower()
        if opsi == "ubah":
            while True:
                Ringkasan(barang_list, jumlah_list)
                index = int(input("Masukkan nomor barang yang ingin diubah: ")) - 1
                if 0 <= index < len(barang_list):
                    tampilan_barang(subsidi)
                    Ringkasan(barang_list, jumlah_list)
                    kode_barang = input("Masukkan kode barang baru (contoh: A.1): ").strip().upper()
                    try:
                        kategori, indeks = kode_barang.split(".")
                        indeks = int(indeks) - 1

                        if kategori == "A" and 0 <= indeks < len(subsidi) - 1:
                            barang_list[index] = subsidi["Benih"][indeks]
                        elif kategori == "B" and 0 <= indeks < len(subsidi) - 1:
                            barang_list[index] = subsidi["Pupuk"][indeks]
                        elif kategori == "C" and 0 <= indeks < len(subsidi) - 1:
                            barang_list[index] = subsidi["Pestisida"][indeks]
                        elif kategori == "D" and 0 <= indeks < len(subsidi) - 1:
                            barang_list[index] = subsidi["Herbisida"][indeks]
                        elif kategori == "E" and 0 <= indeks < len(subsidi):
                            barang_list[index] = subsidi["Barang"][indeks]
                        else:
                            print("Kode barang tidak valid. Pastikan kode sesuai dengan daftar.")
                            continue

                        jumlah_list[index] = input(f"Masukkan jumlah untuk barang '{barang_list[index]}': ").strip()
                        if jumlah_list[index] == "" or 0:
                            print("Jumlah barang tidak boleh kosong. Pastikan jumlah harus di atas '0'.")
                            continue
                    except (ValueError, IndexError):
                        print("Input tidak valid, gunakan format A.1, B.2, dst. Sesuai dengan kode yang ada pada tabel.")
                else:
                    print("Kode barang tidak valid.")

                Ringkasan(barang_list, jumlah_list)

                selesai = input("Ubah barang lain? (y/n): ").strip().lower()
                if selesai != "y":
                    break
        elif opsi == "hapus":
            while True:
                Ringkasan(barang_list, jumlah_list)
                index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
                if 0 <= index < len(barang_list):
                    barang_terhapus = barang_list.pop(index)
                    jumlah_terhapus = jumlah_list.pop(index)
                    print(f"\nBarang '{barang_terhapus}' dengan jumlah {jumlah_terhapus} berhasil dihapus.")

                else:
                    print("Nomor barang tidak valid. Pastikan nomor sesuai dengan daftar.")

                if barang_list:
                    Ringkasan(barang_list, jumlah_list)
                    selesai = input("Hapus barang lain? (y/n): ").strip().lower()
                    if selesai != "y":
                        break
                else:
                    print("\nDaftar barang kosong. Tidak ada barang yang dapat dihapus.")
                    break

def buat_laporan(daerah):
    try:
        buat_l = pd.read_csv('laporan.csv')
        data = buat_l[buat_l['Daerah'] == daerah].iloc[-1]
        data2 = data['status']
        if data2 == 'terkirim':
            return input ('Harap menunggu respon dari Pemerintah Pusat!')
    except IndexError:
        print("Lanjut")

    subsidi = pd.read_csv("subsidi.csv")
    subsidi = subsidi.dropna(axis=1, how='all')
    subsidi = subsidi.dropna(axis=0, how='all')
    subsidi = subsidi.fillna("")

    barang_list = []
    jumlah_list = []
    while True:
        tampilan_barang(subsidi)
        kode_barang = input("\n\n\nMasukkan kode barang untuk memasukkan barang ke laporan (contoh: A.1) dan tekan 'Enter' untuk selesai\nAtau ketik 'kembali' untuk kembali ke menu: ").strip().upper()
        if kode_barang == "":
            if not barang_list:
                print("\nAnda harus memasukkan setidaknya satu barang sebelum selesai.")
                continue 
            break
        elif kode_barang == 'KEMBALI':
            return

        try:
            kategori, indeks = kode_barang.split(".")
            indeks = int(indeks) - 1

            if kategori == "A" and 0 <= indeks < len(subsidi) - 1:
                barang = subsidi["Benih"][indeks]
            elif kategori == "B" and 0 <= indeks < len(subsidi) - 1:
                barang = subsidi["Pupuk"][indeks]
            elif kategori == "C" and 0 <= indeks < len(subsidi) - 1:
                barang = subsidi["Pestisida"][indeks]
            elif kategori == "D" and 0 <= indeks < len(subsidi) - 1:
                barang = subsidi["Herbisida"][indeks]
            elif kategori == "E" and 0 <= indeks < len(subsidi):
                barang = subsidi["Barang"][indeks]
            else:
                print("Kode barang tidak valid. Pastikan kode sesuai dengan daftar.")
                continue
            
            jumlah = input(f"Masukkan jumlah untuk barang '{barang}': ").strip()
            if jumlah == "" or 0:
                print("Jumlah barang tidak boleh kosong. Pastikan jumlah harus di atas '0'.")
                continue
            barang_list.append(barang)
            jumlah_list.append(jumlah)
        except (ValueError, IndexError):
            print("Input tidak valid, gunakan format A.1, B.2, dst. Sesuai dengan kode yang ada pada tabel")

    print("\n" * 9)
    Ringkasan(barang_list, jumlah_list)

    e_Ringkasan(barang_list, jumlah_list, subsidi)

    while True:
        alasan = input("\nMasukkan alasan laporan: ").strip()
        if alasan == "0":
            print("\nKembali ke Menu Utama...")
            return
        if alasan == "":
            print("\nAlasan tidak boleh kosong! Silakan coba lagi.\nAtau ketik '0' untuk membatalkan laporan.")
        else:
            break

    sekarang = datetime.now()
    tanggal = sekarang.strftime("%A, %Y-%m-%d, %H:%M:%S")

    data_laporan = {
        "ID": None,
        "Tanggal": tanggal,
        "Daerah": daerah,
        "Jenis Barang": ";".join(barang_list),
        "Jumlah Barang": ";".join(jumlah_list),
        "Alasan": alasan,
        "status": "terkirim",
        "respon": "Belum ada respon",
    }

    try:
        laporan = pd.read_csv("laporan.csv")
    except FileNotFoundError:
        laporan = pd.DataFrame(columns=["ID", "Tanggal", "Daerah", "Jenis Barang", "Jumlah Barang", "Alasan", "status", "respon"])

    if not laporan.empty:
        data_laporan["ID"] = laporan["ID"].max() + 1
    else:
        data_laporan["ID"] = 1

    laporan = pd.concat([laporan, pd.DataFrame([data_laporan])], ignore_index=True)
    laporan.to_csv("laporan.csv", index=False)

    keys = ["Tanggal", "Daerah", "Jenis Barang", "Jumlah Barang", "Alasan", "status"]
    values = [data_laporan[key] for key in keys]

    print("\n" * 2)
    detail = f"\n╔════════════════════════════════════════════════════════╗\n"
    detail += f"║ {'DETAIL LAPORAN':^54} ║\n"
    detail += "╠════════════════════════════════════════════════════════╣\n"

    lebar_key = 15
    lebar_val = 36

    for key, value in zip(keys, values):
        value = str(value) 
        value_lines = [value[i:i+lebar_val] for i in range(0, len(value), lebar_val)]

        detail +=f"║ {key:<{lebar_key}} : {value_lines[0]:<{lebar_val}} ║\n"

        for line in value_lines[1:]:
            detail += f"║ {'':<{lebar_key}}   {line:<{lebar_val}} ║\n"
    detail += "╚════════════════════════════════════════════════════════╝\n"
    detail += "Tekan 'enter' untuk kembali ke Menu Utama"
    
    input(detail)
