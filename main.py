import pandas as pd
import os
import subprocess
import Fitur_E_commerce as fe
import Fitur_Belanja as fb
import keranjang as ker

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')

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

def registrasi():
    Clear_terminal()
    while True:
        print('✦ ═══════════════════════【 Regitrasi Form 】═══════════════════════ ✦\n')
        nama = input('⊳ Masukkan Nama        : ').capitalize()
        email = input('⊳ Masukkan Email       : ')
        password = input('⊳ Masukkan Password    : ')
        password2 = input('⊳ Konfirmasi Password  : ') 
        if password == password2:
            while True:
                try:
                    Clear_terminal()
                    daerah = ['Nanggroe Aceh Darussalam', 'Sumatera Utara', 'Sumatera Selatan', 'Sumatera Barat', 'Bengkulu', 'Riau', 'Kepulauan Riau', 'Jambi', 'Lampung', 'Bangka Belitung', 'Kalimantan Barat', 'Kalimantan Timur', 'Kalimantan Selatan', 'Kalimantan Tengah', 'Kalimantan Utara', 'Banten', 'DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Daerah Istimewa Yogyakarta', 'Jawa Timur', 'Bali', 'Nusa Tenggara Timur', 'Nusa Tenggara Barat', 'Gorontalo', 'Sulawesi Barat', 'Sulawesi Tengah', 'Sulawesi Utara', 'Sulawesi Tenggara', 'Sulawesi Selatan', 'Maluku Utara', 'Maluku', 'Papua Barat', 'Papua', 'Papua Tengah', 'Papua Pegunungan', 'Papua Selatan', 'Papua Barat Daya']
                    kolom_1 = daerah[:len(daerah)//2]
                    kolom_2 = daerah[len(daerah)//2:]
                    print(f"{'No.' + ' '*2} {'Daerah' + ' '*34} {'No.' + ' '*2} {'Daerah' + ' '*34}")
                    print('==========================================================================================')
                    for index in range(len(kolom_1)):
                        if index < 9:
                            print(f"{str(index+1) + ' '*4} {str(kolom_1[index]) + ' '*(40-len(str(kolom_1[index])))} {str(index+20) + ' '*3} {str(kolom_2[index]) + ' '*34}")
                        else:
                            print(f"{str(index+1) + ' '*3} {str(kolom_1[index]) + ' '*(40-len(str(kolom_1[index])))} {str(index+20) + ' '*3} {str(kolom_2[index]) + ' '*34}")
                        index +=1
                    print('==========================================================================================')
                
                    daerahUser = int(input('⊳ masukkan angka daerah: ')) - 1
                    if  0 <= daerahUser < len(daerah):
                        data = daerah[daerahUser]
                        database = pd.read_csv('./database.csv')
                        if '@gmail.com' not in email: 
                            input(error('Email Yang Anda Masukkan Tidak Falid!'))
                            return ''
                        elif email in database['Email'].values:
                            input(error('Email Yang Anda Masukkan Sudah Digunakan!'))
                            return ''
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
                        Clear_terminal()
                        input(f"""
┌───────────────────────【 DAFTAR BERHASIL 】──────────────────────┐
│                                                                  │
│   ✦ Name         : {nama + ' '*(46-(len(nama))) + '│'}
│   ✦ Email        : {email + ' '*(46-(len(email))) + '│'}
│   ✦ Password     : {password + ' '*(46-(len(password))) + '│'}
│   ✦ Daerah       : {data + ' '*(46-(len(data))) + '│'}
│                                                                  │
│   ─────────────────────────────────────────────────────────────  │
│   Sign-in successful. Press enter to continue.                   │
└──────────────────────────────────────────────────────────────────┘
""")
                        return ''
                    else:
                        input(error('hanya bisa memasukkan angka [1-38]'))
                except ValueError:
                    input(error('hanya bisa memasukkan angka!'))
        else:
            input(error('password 1 dan 2 tidak sama'))

def login():
    Clear_terminal()
    print('✦ ═════════════════════════【 Login Form 】═════════════════════════ ✦\n')
    email = input('⊳ Masukkan Email: ')
    password = input('⊳ Masukkan Password: ')
    Clear_terminal()
    input(f"""┌─────────────────────────【 Login Form 】─────────────────────────┐
│                                                                  │
│   ✦ Email        : {email + ' '*(46-(len(email))) + '│'}
│   ✦ Password     : {password + ' '*(46-(len(password))) + '│'}
│                                                                  │
│   ─────────────────────────────────────────────────────────────  │
│   Press enter to continue.                                       │
└──────────────────────────────────────────────────────────────────┘""")
    database = pd.read_csv('./database.csv')
    if email in database['Email'].values:
        data = database[database['Email'] == email]
        if data['Password'].values[0] == password:
            role = data['Role'].values[0]
        elif data['Password'].values[0] != password:
            input(error('Password salah!'))
            return None, None
    else: 
        input(error('Email tidak ada!. harap registrasi terlebih dahulu!'))
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
    Clear_terminal()
    print("""
╭──────────────────────╮
│    SILAHKAN PILIH    │
├──────────────────────┤
│                      │
│ ✧ 1. Registrasi      │
│ ✧ 2. Login           │
│ ✧ 3. Keluar          │
│                      │
╰──────────────────────╯
    """.strip())
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
                                    fe.main()
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
                                    input(error('Pilihan Anda tidak valid! Harap pilih angka 1, 2, 3, atau 4'))
                        elif role == 'user':
                            pilihan = input('Pilih menu: ')
                            match pilihan:
                                case '1':
                                    Clear_terminal()
                                    print('belanja') 
                                    input('Tekan enter untuk melanjutkan!')
                                    fb.mainn()
                                case '2':
                                    Clear_terminal()
                                    print('keranjang') 
                                    input('Tekan enter untuk melanjutkan!')
                                    ker.mulai()
                                case '3':
                                    Clear_terminal()
                                    print('log out') 
                                    input('Tekan enter untuk melanjutkan!')
                                    break
                                case ValueError:
                                    Clear_terminal()
                                    input(error('Pilihan Anda tidak valid! Harap pilih angka 1, 2, atau 3'))
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
                                    input(error('Pilihan Anda tidak valid! Harap pilih angka 1, 2, atau 3'))
                else:
                    Clear_terminal()
        elif inputan == 3:
                
                break
        else :
            input(error('Pilihan Anda tidak valid! Harap pilih angka 1, 2, atau 3'))
    except (ValueError)  :
        Clear_terminal()
        input(error('Pilihan yang Anda masukkan tidak valid. Harap masukkan angka yang benar.'))