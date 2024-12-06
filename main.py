import pandas as pd
import Fitur_E_commerce_Admin
import laporan
import main_invkepd
from Pengelolaan_Laporan import Pengelolaan_Laporan
from Error_Handling import error, Clear_terminal
import Fitur_E_commerce as fe
import Fitur_Belanja as fb
import keranjang as ker


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
                        database = pd.read_csv('./users.csv')
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
                        datanew.to_csv("users.csv",mode='a',header=False ,index=False)
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
    database = pd.read_csv('./users.csv')
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
    return data['Email'].values[0], data['Daerah'].values[0], role
    

def menu(email, role):
    Clear_terminal()
    pembuka = ''
    data = pd.read_csv('./users.csv')
    data2 = data[data['Email'] == email].iloc[0].to_dict()
    if data2['Role'] == 'kepda':
        data2['Role'] = 'Kepala Daerah'
        teks = f"Selamat datang, Kepala Daerah {data2['Daerah']}!"
        if len(teks) > 49:
            teks = f'''Selamat datang, Kepala Daerah\n{data2['Daerah']}!'''
        pembuka = f"""\n╔═══════════════════════════════════════════════════╗\n║{teks:^51}║\n╚═══════════════════════════════════════════════════╝\n"""
    elif data2['Role'] == 'user':
        pembuka = f'Selamat datang {data2['Name'].upper()} selamat berbelanja :>\n\n'

    pembuka += f"""╔───────────────────────────────────────────────────╗
║                   DATA INFORMASI                  ║
╠───────────────────────────────────────────────────╣
║ ⊳ Name   : {data2['Name'].upper() + ' '*(51-len(data2['Name']) - 12) + '║'}
║ ⊳ Role   : {data2['Role'] + ' '*(51-len(data2['Role']) - 12) + '║'}
║ ⊳ Lokasi : {data2['Daerah'] + ' '*(51-len(data2['Daerah']) - 12) + '║'}
╠───────────────────────────────────────────────────╣\n"""
    if role == 'admin':
        pembuka += f"""║┌─────────────────────────────────────────────────┐║
║│                    LIST MENU                    │║
║├─────────────────────────────────────────────────┤║
║├▶ 1. E-Commerce                                  │║
║├▶ 2. Pengelolaan Laporan                         │║
║├▶ 3. Log Out                                     │║
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
║├▶ 2. Inventaris Daerah                           │║
║├▶ 3. Log Out                                     │║
║└─────────────────────────────────────────────────┘║
╚───────────────────────────────────────────────────╝
"""
    print(pembuka)

Clear_terminal()
print("#======================================================#")
print("#                                                      #")
print("#                 SELAMAT DATANG DI                    #")
print("#                       TAMIL                          #")
print("#                  (Tani Milenial)                     #")
print("#                                                      #")
print("#======================================================#")
print("#                                                      #")
print("#           Tekan [ENTER] untuk Melanjutkan!           #")
print("#                                                      #")
print("#======================================================#")
input("")
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
                username, daerah, role = login()
                if username and daerah and role:
                    while True:
                        menu(username,role)
                        if role == 'admin':
                            pilihan = input('Pilih menu: ')
                            match pilihan: 
                                case '1':
                                    Clear_terminal()
                                    Fitur_E_commerce_Admin.main()
                                case '2':
                                    Clear_terminal()
                                    print(Pengelolaan_Laporan())
                                case '3':
                                    Clear_terminal()
                                    print('Log Out')     
                                    input(f'╔════════════════════════════════════════════════════════╗\n║{'Anda telah logout. Sampai jumpa!'.center(56)}║\n╚════════════════════════════════════════════════════════╝')
                                    break
                                case ValueError:
                                    Clear_terminal()
                                    input(error('Pilihan Anda tidak valid! Harap pilih angka 1, 2, 3, atau 4'))
                        elif role == 'user':
                            pilihan = input('Pilih menu: ')
                            match pilihan:
                                case '1':
                                    Clear_terminal()
                                    fb.mainn()
                                    input('Tekan enter untuk melanjutkan!')
                                case '2':
                                    Clear_terminal()
                                    ker.mulai()
                                    input('Tekan enter untuk melanjutkan!')
                                case '3':
                                    Clear_terminal()
                                    input(f'╔════════════════════════════════════════════════════════╗\n║{'Anda telah logout. Sampai jumpa!'.center(56)}║\n╚════════════════════════════════════════════════════════╝')
                                    input('Tekan enter untuk melanjutkan!')
                                    break
                                case ValueError:
                                    Clear_terminal()
                                    break
                        else: 
                            pilihan = input('Pilih menu: ')
                            match pilihan:
                                case '1':
                                    Clear_terminal()
                                    laporan.buat_laporan(daerah)
                                case '2':
                                    Clear_terminal()
                                    main_invkepd.menu_inventaris(daerah)
                                case '3':
                                    Clear_terminal()
                                    input(f'╔════════════════════════════════════════════════════════╗\n║{'Anda telah logout. Sampai jumpa!'.center(56)}║\n╚════════════════════════════════════════════════════════╝')
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