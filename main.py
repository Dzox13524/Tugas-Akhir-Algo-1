import pandas as pd
import os
import subprocess

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')
    
def registrasi():
    nama = input('Masukkan Nama:')
    email = input('Masukkan Email: ')
    password = input('Masukkan Password: ')
    password2 = input('Masukkan Password Kembali: ') 
    if password == password2:
        list = ['Nanggroe Aceh Darussalam', 'Sumatera Utara', 'Sumatera Selatan', 'Sumatera Barat', 'Bengkulu', 'Riau', 'Kepulauan Riau', 'Jambi', 'Lampung', 'Bangka Belitung', 'Kalimantan Barat', 'Kalimantan Timur', 'Kalimantan Selatan', 'Kalimantan Tengah', 'Kalimantan Utara', 'Banten', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Daerah Istimewa Yogyakarta', 'Jawa Timur', 'Bali', 'Nusa Tenggara Timur', 'Nusa Tenggara Barat', 'Gorontalo', 'Sulawesi Barat', 'Sulawesi Tengah', 'Sulawesi Utara', 'Sulawesi Tenggara', 'Sulawesi Selatan', 'Maluku Utara', 'Maluku', 'Papua Barat', 'Papua', 'Papua Tengah', 'Papua Pegunungan', 'Papua Selatan', 'Papua Barat Daya']
        index = 1
        for i in list:
            print(f'{index}. {i}')
            index +=1
        daerah = int(input('masukkan angka: ')) -1
        if len(list) >= daerah > 0:
            data = list[daerah]
            database = pd.read_csv('./database.csv')
            if '@gmail.com' not in email: return 'email tidak falid!'
            if email in database['Email'].values:return 'email sudah digunakan!'
            No = len(pd.DataFrame(database))
            Newdata = {
                'ID': No+1,
                'Name':nama,
                'Email':email,
                'Password': password,
                'Role': 'user',
                'Daerah':daerah,
                }
            datanew = pd.DataFrame(Newdata, index=[0])
            datanew.to_csv("database.csv",mode='a',header=False ,index=False)
            return 'berhasil daftar!'
        else:
            return 'data tidak ada'
    else:
        return 'password 1 dan 2 tidak sama'

def login():
    email = input('Masukkan Email: ')
    password = input('Masukkan Password: ')
    database = pd.read_csv('./database.csv')
    if email in database['Email'].values:
        data = database[database['Email'] == email]
        username = data['Name'].values[0]
        if data['Password'].values[0] == password:
            role = data['Role'].values[0]
        elif data['Password'].values[0] != password:
            print('password salah')
            return None, None
    else: 
        print('email tidak ada!. harap registrasi terlebih dahulu!')
        return None, None
    return data['Email'].values[0], role

def list_barangS():
    barang = pd.read_csv('./barangdanbahanS.csv')
    text = """
▢---------------------------------------------------▢
║              LIST BARANG DAN BAHAN SUBSIDI        ║
▢---------------------------------------------------▢\n"""
    index = 0
    for i in barang:
        text+= f"│{i.upper()}" + ' '*(53-len(i)-2) + '│'+ '\n'
        for data in barang[i]:
            if str(data) == 'nan':continue
            else:
                text += f"│  ▪ {str(data)}" + ' '*(53-len(str(data))-6) + '│'+ '\n'
                index+=1
        text+= f"├---------------------------------------------------┤\n"
    return text

def menu(email):
    data = pd.read_csv('./database.csv')
    data2 = data[data['Email'] == email].iloc[0].to_dict()
    print(data2)
    pass

print(list_barangS())


# ===============
# while True:
#     print("""1. Registrasi\n2. Login\n3. Keluar""")
#     # try:
#     inputan = int(input('Masukkan nomor [1-3]: '))
#     if inputan == 1:
#             print(registrasi())
#     elif inputan == 2:
#             username, password = login()
#             if username and password:
#                 print('tes')
#             else:
#                 input('Tekan enter untuk melanjutkan!')
#                 Clear_terminal()
#     elif inputan == 3:
#             break
#     else :
#         print('HARUS MEMASUKKAN YANG ADA DIATAS!')
#     # except (ValueError) :
#     #     print('Harus Angka!')
