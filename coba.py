import pandas as pd
total_barang = pd.read_csv('keranjang.csv')
database = pd.read_csv('DataBarang_NS.csv')

for index, row in total_barang.iterrows():
    nama_produk = row['Nama Produk']
    jumlah_produk = row['Jumlah Produk']
    if nama_produk in database['Isi'].values:
        database.loc[database['Isi'] == nama_produk, 'Jumlah'] -= jumlah_produk
database.to_csv('DataBarang_NS.csv', index=False)
