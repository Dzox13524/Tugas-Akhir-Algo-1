import pandas as pd
import os
import subprocess

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

def Daftar_Produk_ECommerce():
        Harga = 20000
        data_barang = {
        'Barang dan Bahan Non Subsidi': ['Benih', '', '', 'Pupuk', '', '', 'Pestisida', '', ''],
        'Isi': ['Tebu', 'Kentang', 'Cabe', 'KCL', 'ZA', 'Magnesium', 'Deltametrin', 'Dithane M-45', 'Omite 570 EC'],
        'Jumlah': [100, 100, 100, 100, 100, 100, 100, 100, 100],
        'Harga/Produk': [Harga,Harga,Harga,Harga,Harga,Harga,Harga,Harga,Harga]
        }
        data_barang = pd.DataFrame(data_barang)
        data_barang.to_csv('DataBarang_NS.csv', index=False)
        database = pd.read_csv('DataBarang_NS.csv')
        hiasan = '✦ ═══════════════════════【 Data Barang dan Bahan Non Subsidi 】═══════════════════════ ✦\n'
        print(hiasan)
        print(f"{'No.' + ' '*2} {'Barang dan Bahan Non Subsidi' + ' '*10} {'Isi' + ' '*12} {' '*2 + 'Jumlah'} {' '*4 + 'Harga/Produk' + ' '*5}")
        print('═════════════════════════════════════════════════════════════════════════════════════════')  
        for index, (barang, isi, jumlah, harga) in enumerate(zip(database['Barang dan Bahan Non Subsidi'], database['Isi'], database['Jumlah'], database['Harga/Produk'])):
                
                print(f"{index + 1:<4} {barang:<39} {isi:<17} {jumlah:<10} {harga}")
        print('═════════════════════════════════════════════════════════════════════════════════════════')     

def edit():
    while True:
        hiasan = '✦ ═════════════════════════════════════════════════════════════════════════════════════ ✦'
        print(hiasan)
        print(" "*(len(hiasan)//2 - 10//2) + "Ubah Harga")
        print(" "*(len(hiasan)//2 - 14//2) + "Restock Barang")
        print(" "*(len(hiasan)//2 - 8//2) + "Kembali")
        print(hiasan)
        global pilihan_admin
        pilihan_admin = input("Pilih Menu: ")
        pilihan_admin = pilihan_admin.upper()
        match pilihan_admin:
            case "UBAH HARGA":
                Clear_terminal()
                ubah_harga()
                break
            case "RESTOCK BARANG":
                Clear_terminal()
                restock_barang()
                break
            case "KEMBALI":
                Clear_terminal()
                menu()
                break
            case _:
                Clear_terminal()
                print("Pilihan anda tidak valid: ")
                continue
        return pilihan_admin
def gaya_tulisan():
    pesan_invalid = "Pilihan anda tidak valid!!!"
    pesan_invalid = pesan_invalid.upper()
    panjang_kotak = len(pesan_invalid) + 4
    print("─" * panjang_kotak)  
    print(f"│ {pesan_invalid} │")  
    print("─" * panjang_kotak)
def ubah_harga():
    Daftar_Produk_ECommerce()
    while True:
        ubah_harga = input("Pilih Produk yang ingin diubah harganya: ")
        data_barang = pd.read_csv('DataBarang_NS.csv')
        if ubah_harga not in data_barang['Isi'].values:
            Clear_terminal()
            Daftar_Produk_ECommerce()
            print("Produk tidak ditemukan")
            print("TOLONG SESUAIKAN DENGAN ISI TABEL")
            continue
        
        kata = f"Produk yang ingin diubah adalah {ubah_harga}"
        print("──────────────────────────────────────────────────────────────────────────────────────")
        print("!" * 34 + " KONFIRMASI ULANG " + "!" * 34)
        print("──────────────────────────────────────────────────────────────────────────────────────")
        print(' ' * (86//2 - (len(kata)//2)) + kata)
        print("──────────────────────────────────────────────────────────────────────────────────────")
        konfirmasi = input("Yakin ingin mengubah barang tersebut? (Y/N): ")

        match konfirmasi.upper():
            case "Y":
                while True:
                    harga_baru = input("Masukkan harga baru: ")
                    if not harga_baru.isdigit():  
                        print("Harga harus berupa angka tanpa titik atau koma.")
                        continue  
                    
                    try:
                        harga_baru = float(harga_baru)
                        data_barang.loc[data_barang['Isi'] == ubah_harga, 'Harga/Produk'] = harga_baru
                        pesan = f"Harga produk '{ubah_harga}' berhasil diubah menjadi {harga_baru}."
                        panjang_kotak = len(pesan) + 4  
                        print("*" * panjang_kotak)  
                        print(f"* {pesan} *")  
                        print("*" * panjang_kotak)
                        data_barang.to_csv('DataBarang_NS.csv', index=False)
                        break  
                    except ValueError:
                        print("Terjadi kesalahan saat mengubah harga.")
                        continue
            case "N":
                Clear_terminal()
                Daftar_Produk_ECommerce()
                edit()
                break
            case _:
                Clear_terminal()
                gaya_tulisan()
                while True:
                    tidak_valid = input("TEKAN ENTER UNTUK MELANJUTKAN")
                    if tidak_valid != "":
                        continue
                    else:
                        Clear_terminal()
                        Daftar_Produk_ECommerce()
                        break
                continue
        return data_barang


def restock_barang():
    pass

def main():
    Daftar_Produk_ECommerce()
    edit()
main()