import pandas as pd
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
gaya_keranjang()