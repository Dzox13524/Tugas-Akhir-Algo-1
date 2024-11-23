import pandas as pd


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
        else:
            print( 'password 1 dan 2 tidak sama')
print(registrasi())