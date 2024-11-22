list = ['Nanggroe Aceh Darussalam', 'Sumatera Utara', 'Sumatera Selatan', 'Sumatera Barat', 'Bengkulu', 'Riau', 'Kepulauan Riau', 'Jambi', 'Lampung', 'Bangka Belitung', 'Kalimantan Barat', 'Kalimantan Timur', 'Kalimantan Selatan', 'Kalimantan Tengah', 'Kalimantan Utara', 'Banten', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Daerah Istimewa Yogyakarta', 'Jawa Timur', 'Bali', 'Nusa Tenggara Timur', 'Nusa Tenggara Barat', 'Gorontalo', 'Sulawesi Barat', 'Sulawesi Tengah', 'Sulawesi Utara', 'Sulawesi Tenggara', 'Sulawesi Selatan', 'Maluku Utara', 'Maluku', 'Papua Barat', 'Papua', 'Papua Tengah', 'Papua Pegunungan', 'Papua Selatan', 'Papua Barat Daya']
for index, provinsi in enumerate(list, start= 1):
    print(f"{index}. {provinsi}")

while True:
    try:
        daerah = int(input('pilih daerah anda: '))
        if 1 <= daerah <= index:
            data_user = list[daerah-1]
            print(f"Daerahmu adalah {list[daerah-1]}")
            break
        else:
            print(f"Nomor yang tersedia adalah 1 - {index}")
    except ValueError:
        print("Hanya menerima input nomor urut dari daerahmu")