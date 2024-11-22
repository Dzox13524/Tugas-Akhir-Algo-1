import pandas as pd
import os
import subprocess


def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')
    
def registrasi2():
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
                'Daerah':data,
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
            print('password salah!')
            Clear_terminal()
    else: 
        print('email tidak ada!. harap registrasi terlebih dahulu!')
        Clear_terminal()
    return username, role

while True:
    # Clear_terminal()
    print("""1. Registrasi\n2. Login\n3. Keluar""")
    try:
        inputan = int(input('Masukkan nomor [1-3]: '))
        # Clear_terminal()
        if inputan == 1:
            print(registrasi2())
        if inputan == 2:
            email = input('Masukkan Email: ')
            password = input('Masukkan Password: ')
            print(login(email, password))
        if inputan == 3:
            break
    except (ValueError) :
        print('Harus Angka!')
