import pandas as pd
import os
import time

def success_message(message):
    atas = "╭──────────────────────────────────────────────────────────────╮"
    bawah = "╰──────────────────────────────────────────────────────────────╯"
    padding = len(message) + 21
    middle = f"│ 🎉 SUCCESS: {message}{' ' * (padding - 32)}│"
    return f"\n{atas}\n{middle}\n{bawah}"

def gaya_keranjang():
    global total_barang
    total_barang = pd.read_csv('keranjang.csv')
    hiasan = '✦ ══════════════════════════【 Data Isi Keranjang Saat Ini 】══════════════════════════ ✦\n'
    print(hiasan)
    print(f'{'No.' + ' '*1} {'Nama Produk' + ' '*28} {'Jumlah Produk'}')
    print('═════════════════════════════════════════════════════════════════════════════════════════')  
    for index, (nama_produk,jumlah_produk) in enumerate(zip(total_barang['Nama Produk'], total_barang['Jumlah Produk'])):
        print(f'{index + 1:<4} {nama_produk:<39} {jumlah_produk:<17}')
    print('═════════════════════════════════════════════════════════════════════════════════════════') 

def error(messages):
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

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

def gaya_progress(pesan):
    print(pesan) 
    for i in range(101):
        print(f"\rProgress: {i}%", end='', flush=True)
        time.sleep(0.05)

def keranjang():
    global total_barang
    total_barang = pd.read_csv('keranjang.csv')
    while True:
        try:
            gaya_keranjang()
            edit = input('Kurangi isi keranjang?\n(y/n): ')
            edit = edit.replace(" ","")
            if edit.lower() == 'y':
                Clear_terminal()
                gaya_keranjang()
                pilih = input("Pilih barang yang ingin di kurangi: ")
                if pilih not in total_barang['Nama Produk'].values:
                    print(error('Barang tidak ditemukan\nSilahkan belanja terlebih dahulu'))
                    continue
                else:
                    barang_edit = int(input("Masukkan jumlah barang yang ingin di kurangi: "))
                    total_barang.loc[total_barang['Nama Produk'] == pilih, 'Jumlah Produk'] -= barang_edit
                    total_barang.to_csv('keranjang.csv',index=False)
                    continue
            elif edit.lower() == 'n':
                Clear_terminal()
                gaya_keranjang()
                print(gaya_progress('Proses Checkout: '))
                for index, row in total_barang.iterrows():
                    nama_produk = row['Nama Produk']
                    jumlah_produk = row['Jumlah Produk']
                    database = pd.read_csv('DataBarang_NS.csv')
                    if nama_produk in database['Isi'].values:
                        database.loc[database['Isi'] == nama_produk, 'Jumlah'] += jumlah_produk
                    else:
                        print(error(f'Produk {nama_produk} tidak ditemukan di database.'))
                database.to_csv('DataBarang_NS.csv', index=False)
                print(success_message('Produk Berhasil Ditambahkan!!!'))
                total_barang = pd.DataFrame(columns=['No', 'Nama Produk', 'Jumlah Produk'])
                total_barang.to_csv('keranjang.csv', index=False)
                break
            else:
                print(error('Pilihan tidak tersedia'))
                continue
        except ValueError:
            Clear_terminal()
            print(error('Input tidak valid'))
            continue
    return

def mulai():
    Clear_terminal()
    keranjang()
    return
