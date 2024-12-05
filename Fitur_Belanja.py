import pandas as pd
import os
import subprocess
import time
from time import sleep
import Fitur_E_commerce as fe

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

def welcome_message():
    clear_terminal()
    panjang_terminal = os.get_terminal_size().columns
    padding = panjang_terminal//2 - 33
    atas = '*'*padding + "╔══════════════════════════════════════════════════════════════╗" + '*'*(padding+2)
    bawah = '*'*padding +"╚══════════════════════════════════════════════════════════════╝" + '*'*(padding+2)
    tengah ='*'*padding + "║                  SELAMAT DATANG DI TOKO KAMI                 ║" + '*'*(padding+2)
    tengah2 ='*'*padding +"║                   ✨ SELAMAT BERBELANJA ✨                   ║" + '*'*(padding+2)
    return f"\n{atas}\n{tengah}\n{tengah2}\n{bawah}"

def inpo(pesan):
    panjang_terminal = os.get_terminal_size().columns
    panjang_pesan = len(pesan)
    padding = (panjang_terminal - panjang_pesan) // 2
    panjang_garis = "─" * panjang_terminal
    return f"{panjang_garis}\n{' ' * padding}{pesan}\n{panjang_garis}"

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
    
    clear_terminal()
    return f'{atas}{tengah}\n{bawah}'

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

def daftar_produk():
    while True:
        clear_terminal()
        print(welcome_message())
        print(inpo("TEKAN ENTER UNTUK MELANJUTKAN"))
        enter1 = input('')
        while enter1 != '':
            clear_terminal()
            print(welcome_message())
            print(inpo("TEKAN ENTER BUKAN YANG LAIN"))
            enter1 = input('')
            continue
        while True:
            clear_terminal()
            fe.Data_baru()
            gaya_keranjang()
            global database
            database = pd.read_csv('DataBarang_NS.csv')
            produk = input("Masukkan Nama Produk tertera yang ingin di beli (Tabel Isi): ")
            try:
                if produk not in database['Isi'].values:
                    print(error("INPUT HARUS SESUAI PRODUK TERTERA DI KOLOM ISI"))
                    input()
                    continue
                else:
                    clear_terminal()
                    klasifikasi = database.loc[database['Isi'] == produk, 'Barang dan Bahan Non Subsidi'].values[0]
                    jumlah_sekarang = database.loc[database['Isi'] == produk, 'Jumlah'].values[0]
                    print(inpo(f"Produk yang dipilih adalah {klasifikasi} {produk}"))
                    print(inpo("TEKAN ENTER UNTUK MELANJUTKAN"))
                    enter1 = input('')
                    while enter1 != '':
                        clear_terminal()
                        print(inpo("TEKAN ENTER BUKAN YANG LAIN"))
                        enter1 = input('')
                        continue
                    break
            except ValueError:
                error("Pilihan Tidak Valid")
                input()
                continue
        while True:
            clear_terminal()
            try:
                fe.Data_baru()
                gaya_keranjang()
                jumlah_barang = int(input(f"{produk} saat ini: {jumlah_sekarang}\nMasukkan jumlah produk yang ingin dibeli: "))
                global total_barang
                total_barang = pd.read_csv('keranjang.csv')
                barang_keranjang = total_barang.loc[total_barang['Nama Produk'] == produk, 'Jumlah Produk'].values[0]
                if jumlah_barang + barang_keranjang > jumlah_sekarang:
                    print(error("Jumlah yang diinput melebihi jumlah yang tersedia"))
                    input()
                    daftar_produk()
                else:
                    fe.gaya_progress(f'Memasukkan {produk} ke keranjang')
                    if produk in total_barang['Nama Produk'].values:
                        if total_barang.loc[total_barang['Nama Produk'] == produk, 'Jumlah Produk'] + jumlah_barang > jumlah_sekarang:
                            print(error('Jumlah Input Di keranjang melebihi jumlah yang tersedia'))
                            continue
                        else:
                            total_barang.loc[total_barang['Nama Produk'] == produk, 'Jumlah Produk'] += jumlah_barang
                            total_barang.to_csv('keranjang.csv',index=False)
                            break
                    else:
                        keranjang = {
                            'No' : len(total_barang) +1,
                            'Nama Produk' : produk,
                            'Jumlah Produk' : jumlah_barang,
                        }
                        checkout = pd.DataFrame(keranjang, index=[0])
                        total_barang = pd.concat([total_barang, checkout], ignore_index=True)
                        total_barang.to_csv('keranjang.csv', index=False)
                        clear_terminal()
            except ValueError:
                print(error("INPUT HARUS BERUPA BILANGAN BULAT DAN HANYA ANGKA"))
                enter1 = input('')
                while enter1 != '':
                        clear_terminal()
                        print(welcome_message())
                        print(inpo("TEKAN ENTER BUKAN YANG LAIN"))
                        enter1 = input('')
                        continue
                continue
        print(success_message('Produk Berhasil Ditambahkan!!!'))
        while True:
            konfirmasi_belanja = input('Lanjutkan Berbelanja?\n[y/n]: ')
            if konfirmasi_belanja.lower() == 'y':
                break
            elif konfirmasi_belanja.lower() == 'n':
                return 'n'
            else:
                print(error("Pilihan Tidak Valid"))
                input('')
                continue
        continue



def mainn():
    while True:
        clear_terminal()
        if daftar_produk() == "n":
            break
        return
mainn()