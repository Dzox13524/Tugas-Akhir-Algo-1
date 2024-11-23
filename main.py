import pandas as pd
import os
import subprocess

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')

text_login = """
=====================================================

:::        ::::::::   :::::::: ::::::::::: ::::    :::
:+:       :+:    :+: :+:    :+:    :+:     :+:+:   :+:
+:+       +:+    +:+ +:+           +:+     :+:+:+  +:+
+#+       +#+    +:+ :#:           +#+     +#+ +:+ +#+
+#+       +#+    +#+ +#+   +#+#    +#+     +#+  +#+#+#
#+#       #+#    #+# #+#    #+#    #+#     #+#   #+#+#
########## ########   ######## ########### ###    ####
====================================================="""
def registrasi():
    while True:
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
            while True:
                try:
                    daerah = int(input('masukkan angka: ')) - 1
                    if  0 <= daerah <= len(list):
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
                            'Daerah':data,
                            }
                        print(Newdata)
                        datanew = pd.DataFrame(Newdata, index=[0])
                        datanew.to_csv("database.csv",mode='a',header=False ,index=False)
                        return 'berhasil daftar!'
                except ValueError:
                    input(ValueError)
        else:
            print( 'password 1 dan 2 tidak sama')

def login():
    Clear_terminal()
    print(text_login + '\n\n')
    print("""╭────〔 login menu 〕────☉
│""")
    email = input('├▷ Email: ')
    print('│')
    password = input('├▷ Masukkan Password: ')
    print("""│
╰────☉""")
    input('Tekan enter untuk melanjutkan')
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
╔───────────────────────────────────────────────────╗
║             LIST BARANG DAN BAHAN SUBSIDI         ║
╠───────────────────────────────────────────────────╣\n"""
    index = 0
    loop = 0
    for i in barang:
        text+= f"║{i.upper()}" + ' '*(53-len(i)-2) + '║'+ '\n'
        for data in barang[i]:
            if str(data) == 'nan':continue
            else:
                text += f"║  ▪ {str(data)}" + ' '*(53-len(str(data))-6) + '║'+ '\n'
                index+=1
        if loop < len(barang) :
            text+= f"╠───────────────────────────────────────────────────╣\n"
            loop += 1
        else : 
            text+= f"╚───────────────────────────────────────────────────╝\n"
    return text

def menu(email, role):
    Clear_terminal()
    data = pd.read_csv('./database.csv')
    data2 = data[data['Email'] == email].iloc[0].to_dict()
    pembuka = f'Selamat datang {data2['Name'].upper()} selamat berbelanja :>\n\n'
    pembuka += f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {data2['Name'].upper() + ' '*(51-len(data2['Name']) - 12) + '║'}
║ ⊳ Role   : {data2['Role'] + ' '*(51-len(data2['Role']) - 12) + '║'}
║ ⊳ Lokasi : {data2['Daerah'] + ' '*(51-len(data2['Daerah']) - 12) + '║'}
║ ⊳ Pesan  : 0                                      ║
╠───────────────────────────────────────────────────╣\n"""
    if role == 'admin':
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║
║├▶ 1. Feedback                                    │║
║├▶ 2. E-Commerce                                  │║
║├▶ 3. Inventaris Admin                            │║
║├▶ 4. Log Out                                     │║
║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    elif role == 'user':
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║
║├▶ 1. Belanja                                     │║
║├▶ 2. Keranjang                                   │║
║├▶ 3. Log out                                     │║
║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    else :
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║
║├▶ 1. Request Barang                              │║
║├▶ 2. Inventaris                                  │║
║├▶ 3. Log Out                                     │║
║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    print(pembuka)

# ===============
while True:
    print("""1. Registrasi\n2. Login\n3. Keluar""")
    try:
        inputan = int(input('Masukkan nomor [1-3]: '))
        if inputan == 1:
                print(registrasi())
        elif inputan == 2:
                username, role = login()
                if username and role:
                    while True:
                        menu(username,role)
                        if role == 'admin':
                            pilihan = input('Pilih menu: ')
                            match pilihan: 
                                case '1':
                                    Clear_terminal()
                                    print("Feedback")
                                    input('Tekan enter untuk melanjutkan!')
                                case '2':
                                    Clear_terminal()
                                    print('E-Commerce')
                                    input('Tekan enter untuk melanjutkan!')
                                case '3':
                                    Clear_terminal()
                                    print('Inventaris Admin')     
                                    input('Tekan enter untuk melanjutkan!')                           
                                case '4':
                                    Clear_terminal()
                                    print('Log Out')     
                                    input('Tekan enter untuk melanjutkan!')
                                    break
                                case ValueError:
                                    Clear_terminal()
                                    print('Harus angka 1-4')
                                    input('Tekan enter untuk melanjutkan!')
                        elif role == 'user':
                            pilihan = input('Pilih menu: ')
                            match pilihan:
                                case '1':
                                    Clear_terminal()
                                    print('belanja') 
                                    input('Tekan enter untuk melanjutkan!')
                                case '2':
                                    Clear_terminal()
                                    print('keranjang') 
                                    input('Tekan enter untuk melanjutkan!')
                                case '3':
                                    Clear_terminal()
                                    print('log out') 
                                    input('Tekan enter untuk melanjutkan!')
                                    break
                                case ValueError:
                                    Clear_terminal()
                                    print('Harus angka 1-3')
                                    input('Tekan enter untuk melanjutkan!')
                        else: 
                            pilihan = input('Pilih menu: ')
                            match pilihan:
                                case '1':
                                    Clear_terminal()
                                    print(list_barangS()) 
                                    input('Tekan enter untuk melanjutkan!')
                                case '2':
                                    Clear_terminal()
                                    print('Inventaris') 
                                    input('Tekan enter untuk melanjutkan!')
                                case '3':
                                    Clear_terminal()
                                    print('log out') 
                                    input('Tekan enter untuk melanjutkan!')
                                    break
                                case ValueError:
                                    Clear_terminal()
                                    print('Harus angka 1-3')
                                    input('Tekan enter untuk melanjutkan!')
                else:
                    input('Tekan enter untuk melanjutkan!')
                    Clear_terminal()
        elif inputan == 3:
                break
        else :
            print('HARUS MEMASUKKAN YANG ADA DIATAS!')
    except (ValueError)  :
        Clear_terminal()
        print('Harus Angka!')
        input('klik enter untuk melanjutkan')
