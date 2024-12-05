import pandas as pd #Fitur Import
import os 
import subprocess
import time
from time import sleep

def Clear_terminal():#Membersihkan Terminal
    if os.name == 'nt':
        os.system('cls')
    else:   
        subprocess.call('clear')
        
def gaya_tulisan(pesan,pesan2,pesan3):#3 Pesan
    panjang_terminal = os.get_terminal_size().columns
    panjang_pesan = len(pesan) + 4
    panjang_pesan2 = len(pesan2)
    panjang_pesan3 = len(pesan3)
    padding = (panjang_terminal - panjang_pesan) // 2
    padding2 = (panjang_terminal - panjang_pesan2) // 2
    padding3 = (panjang_terminal - panjang_pesan3) // 2
    panjang_garis = "─" * panjang_terminal
    print(panjang_garis)
    print(" " * padding + " "*2 + pesan + " " * padding)
    print(" " * padding2 + pesan2 + " " * padding2)
    print(" " * padding3 + pesan3 + " " * padding3)
    print(panjang_garis)

def gaya_tulisan2(pesan): #Tanda Seru
    panjang_terminal = os.get_terminal_size().columns
    panjang_pesan = len(pesan) + 2
    padding = (panjang_terminal - panjang_pesan) // 2
    panjang_garis = "─" * panjang_terminal
    print(panjang_garis)
    print("!" * padding + " " + pesan + " " + "!" * padding)
    print(panjang_garis)

def gaya_tulisan3(pesan): #Clear
    panjang_terminal = os.get_terminal_size().columns
    panjang_pesan = len(pesan) + 2
    padding = (panjang_terminal - panjang_pesan) // 2
    panjang_garis = "─" * panjang_terminal
    print(panjang_garis)
    print(" " * padding + " " + pesan + " " + " " * padding)
    print(panjang_garis)

def gaya_loading(): #Loading
    panjang_terminal = os.get_terminal_size().columns
    padding = (panjang_terminal - 13) // 2
    pesan_input = "."*padding + "!!!LOADING!!!" + "."*padding
    for char in pesan_input:
        print(char, end="", flush=True)
        time.sleep(0.1)

def error(messages): #Untuk Error Handling
    atas = """╔════════════════════!!! ERROR DETECTED !!!════════════════════╗
║                                                              ║"""
    tengah = ''
    bawah = """║                                                              ║
╠──────────────────────────────────────────────────────────────╣
║   Press enter to continue.                                   ║
╚══════════════════════════════════════════════════════════════╝
"""
    data = messages.split()
    hasil = []
    result = '║ ⚠ ERROR: '
    index = 0

    for i in data:
        if len(result) + len(i) + 1 <= 63:
            result += i + " "
            index += 1
        else:
            result += ' ' * (63 - len(result)) + '║'
            hasil.append(result)
            result = '║ '
            result += i + " "

    if result.strip() != '║':
        result += ' ' * (63 - len(result)) + '║'
        hasil.append(result)

    for i in hasil:
        tengah += f"\n{i.strip()}"
    
    Clear_terminal()
    return f'{atas}{tengah}\n{bawah}'

def gaya_progress(pesan):#Progress Dalam Persen
    print(pesan) 
    for i in range(101):
        print(f"\rProgress: {i}%", end='', flush=True)
        time.sleep(0.05)

def Data_baru():
    global database
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
        pilihan_admin = input("Pilih Menu: ").upper()
        match pilihan_admin:
            case "UBAH HARGA":
                Clear_terminal()
                ubah_harga()
                return
            case "RESTOCK BARANG":
                Clear_terminal()
                restock_barang()
                return
            case "KEMBALI":
                return "KEMBALI"  
            case _:
                Clear_terminal()
                print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT SESUAI PILIHAN"))
                input('')
                Clear_terminal()
                return

def ubah_harga():
    while True:
        Clear_terminal()
        Data_baru()
        global database
        global Ubah_harga
        Ubah_harga = input("Pilih Produk yang ingin diubah harganya: ")
        database = pd.read_csv('DataBarang_NS.csv')
        if Ubah_harga not in database['Isi'].values:
            Clear_terminal()
            gaya_tulisan("PRODUK TIDAK DITEMUKAN!",'TOLONG KETIK SESUAI NAMA PRODUK','TEKAN ENTER UNTUK MELANJUTKAN')
            input('')
            continue
        else:
            break
    Clear_terminal()
    gaya_tulisan2(f"PRODUK YANG INGIN DIUBAH HARGANYA ADALAH {Ubah_harga}")
    gaya_loading()
    Clear_terminal()
    while True: 
        Data_baru()
        harga_baru = input("Masukkan Harga Baru: ")
        if not harga_baru.isdigit():
            Clear_terminal()
            gaya_tulisan("HARGA HARUS BERUPA ANGKA!","TANPA TITIK, KOMA, SPASI DAN ALPHABET!","TEKAN ENTER UNTUK MELANJUTKAN")
            input('')
            Clear_terminal()
            continue
        try:
            harga_baru = int(harga_baru)
            database.loc[database["Isi"] == Ubah_harga, "Harga/Produk"] = int(harga_baru)
            database.to_csv('DataBarang_NS.csv', index=False)
            Clear_terminal()
            gaya_tulisan2(F"HARGA {Ubah_harga} SEDANG DIUBAH MENJADI {harga_baru}")
            gaya_loading()
            Clear_terminal()
            gaya_tulisan2('TEKAN ENTER UNTUK MELANJUTKAN')
            input('TEKAN ENTER')
            gaya_progress()
            Clear_terminal()
            gaya_tulisan3(F"HARGA BERHASIL DIUBAH, NAMA PRODUK ADALAH {Ubah_harga} MENJADI RP. {harga_baru}, TEKAN ENTER UNTUK MELANJUTKAN")        
            input("")
            Clear_terminal()
            break
        except ValueError:
            Clear_terminal()
            print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT SESUAI PILIHAN"))
            input("")
            Clear_terminal()
            continue
    while True:
        Clear_terminal()
        gaya_tulisan3("LANJUTKAN UBAH HARGA???")
        print("\n1. Ya\n2. Tidak")
        jawaban = input("Input (Hanya Angka): ")
        try:
            if jawaban == "1":
                ubah_harga()
            elif jawaban == "2":
                Clear_terminal()
                return
            else:
                Clear_terminal()
                print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT SESUAI PILIHAN"))
                input('')
                Clear_terminal()
                continue
        except ValueError:
            Clear_terminal()
            print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT SESUAI PILIHAN"))
            input("")
            Clear_terminal()
            continue
        return

def restock_barang():
    while True:
        Clear_terminal()
        Data_baru()
        global barang_restock
        global database
        while True:
            Clear_terminal()
            Data_baru()
            global barang_restock
            global database
            database = pd.read_csv('DataBarang_NS.csv')
            barang_restock = input("Pilih Barang yang Ingin direstock: ")
            try:
                if barang_restock not in database["Isi"].values:
                    Clear_terminal()
                    print(error("BARANG TIDAK ADA DI DATABASE!!!\nPASTIKAN INPUT SESUAI NAMA BARANG"))
                    input('')
                    continue
                else:
                    break
            except ValueError:
                Clear_terminal()
                print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT SESUAI PILIHHAN"))
                continue
        Clear_terminal()
        gaya_tulisan2(f"BARANG YANG INGIN DIRESTOCK ADALAH {barang_restock}")
        gaya_tulisan2("TEKAN ENTER UNTUK MELANJUTKAN")
        input('')
        while True:
            try:
                Clear_terminal()
                Data_baru()
                global jumlah_restock
                jumlah_restock = input(f"Masukkan Jumlah {barang_restock} yang Ingin direstock: ")
                if not jumlah_restock.isdigit():
                    Clear_terminal()
                    print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT HANYA BERISI ANGKA DAN TANPA SPASI"))
                    input('')
                    continue
                else:
                    break
            except ValueError:
                Clear_terminal()
                print(error("INPUT TIDAK VALID!!! PASTIKAN INPUT HANYA BERISI ANGKA DAN TANPA SPASI"))
                input('')
                continue
        jumlah_restock = int(jumlah_restock)
        database.loc[database["Isi"] == barang_restock, "Jumlah"] += jumlah_restock
        database.to_csv('DataBarang_NS.csv', index=False)
        Clear_terminal()
        gaya_tulisan2(f"SEDANG MENAMBAH {jumlah_restock} {barang_restock}")
        gaya_loading()
        Clear_terminal()
        gaya_tulisan3("TEKAN ENTER UNTUK MELANJUTKAN")
        input('ENTER:')
        gaya_progress()
        Clear_terminal()
        gaya_tulisan2(F"{barang_restock} BERHASIL DIRESTOCK MENJADI {database.loc[database['Isi'] == barang_restock,'Jumlah'].values[0]}")
        gaya_tulisan3("TEKAN ENTER UNTUK MELANJUTKAN")
        input('')
        while True:
            Clear_terminal()
            gaya_tulisan3("LANJUTKAN UBAH RESTOCK BARANG???")
            print("\n1. Ya\n2. Tidak")
            jawaban = input("Input (Hanya Angka): ")
            try:
                if jawaban == "1":
                    Clear_terminal()
                    restock_barang()
                    break
                elif jawaban == "2":
                    Clear_terminal()
                    return
                else:
                    Clear_terminal()
                    print(error("INPUT TIDAK VALID!!! MASUKKAN HANYA ANGKA 1 ATAU 2"))
                    input('')
                    continue
            except ValueError:
                Clear_terminal()
                print(error("INPUT TIDAK VALID!!! MASUKKAN HANYA ANGKA 1 ATAU 2"))
                input('')
                continue
        return



def main():
    while True:
        Data_baru()
        if edit() == "KEMBALI":
            break
    return