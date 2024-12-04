import pandas as pd
from Error_Handling import error, Clear_terminal

listLaporan = {}
def List_Inventaris():
    data = pd.read_csv('./laporan.csv')
    index = 0
    header = """╭════════════════════════════════════════════════════════════════════════════════════════════════════════╮
║                                              LIST LAPORAN                                              ║
╠═══════╦════════════════════════════╦════════════════════════════════════════╦══════════════╦═══════════╣
║   NO  ║           DAERAH           ║              LAST MESSAGE              ║ JUMLAH PESAN ║  PENDING  ║
╠═══════╬════════════════════════════╬════════════════════════════════════════╬══════════════╬═══════════╣\n"""

    for i in range(len(data['Daerah'])) :      
        if str(data['Daerah'][i]) not in listLaporan:
            tanggal = data[data['Daerah'] == data['Daerah'][i]].iloc[0].to_dict()
            listLaporan[str(data['Daerah'][i])] = {
                "total_pesan": 1,
                "pending": 0, 
                'date': tanggal['Tanggal'], 
                'date': tanggal['Tanggal'], 
                'daerah':tanggal['Daerah'], 
                'data':[tanggal]
                }
            if tanggal['status'] == 'terkirim':
                listLaporan[str(data['Daerah'][i])]['pending'] += 1
        else:
            tanggal = data[data['Daerah'] == data['Daerah'][i]].iloc[(listLaporan[str(data['Daerah'][i])]['total_pesan'])].to_dict()
            listLaporan[str(data['Daerah'][i])]["total_pesan"] += 1
            listLaporan[str(data['Daerah'][i])]['data'].append(tanggal)
            if tanggal['status'] == 'terkirim':
                listLaporan[str(data['Daerah'][i])]['pending'] += 1
            continue

    for i in listLaporan:
        index += 1
        header += f"║{str(index).center(7)}║{listLaporan[i]['daerah'].center(28)}║{listLaporan[i]['date'].center(40)}║{str(listLaporan[i]['total_pesan']).center(14)}║{str(listLaporan[i]['pending']).center(11)}║\n"
        if index == len(listLaporan):
            header += '╰═══════╩════════════════════════════╩════════════════════════════════════════╩══════════════╩═══════════╯'
    return header

def remove_keys(data): 
    arr = []
    for i in data:
        arr.append(data[i])
    return arr 


def inventaris_Daerah(nomer):
    list_laporan = remove_keys(listLaporan)
    text = f"""
╭═══════════════════════════════════════════════════════════════════════════════════════════════════════╮
║{('INVENTARIS ' + (list_laporan[nomer]['daerah']).upper()).center(103)}║
╠═══════╦════════════════════════════════════════╦════════════════════╦════════════════════╦════════════╣
║   NO  ║                 TANGGAL                ║ BAHAN ATAU BARANG  ║   JUMLAH BARANG    ║   STATUS   ║
╠═══════╬════════════════════════════════════════╬════════════════════╬════════════════════╬════════════╣\n"""
    no = 0
    for i in list_laporan[nomer]['data']:
        barang = i['Jenis Barang'].split(';')
        jumlah = i['Jumlah Barang'].split(';')
        if i['status'] == 'terkirim':
            i['status'] = 'Pending'
        text += f"║{str(no+1).center(7)}║{i['Tanggal'].center(40)}║{(barang[0]).center(20)}║{jumlah[0].center(20)}║{(i['status']).center(12)}║\n"
        for i in range(1, len(barang)):
            text += f"║       ║                                        ║{(barang[i]).center(20)}║{jumlah[i].center(20)}║            ║\n"
        if len(list_laporan[nomer]['data']) != no+1:
            text +=  "╠═══════╬════════════════════════════════════════╬════════════════════╬════════════════════╬════════════╣\n"
        else:
            text +=  '╰═══════╩════════════════════════════════════════╩════════════════════╩════════════════════╩════════════╯'
        no += 1
    return text

def data_daerah(daerah):
    data = pd.read_csv('./laporan.csv')
    list_barang = data[(data['Daerah'] == daerah) & (data['status'] == 'acc')]['Jenis Barang'].values
    jumlah_barang = data[(data['Daerah'] == daerah) & (data['status'] == 'acc')]['Jumlah Barang'].values
    dict_barang = {}
    for i in range(len(list_barang)):
        barang = list_barang[i].split(';')
        jumlah = jumlah_barang[i].split(';')
        for data in range(len(barang)):
            if barang[data] not in dict_barang:
                dict_barang[barang[data]] = int(jumlah[data])
            else:
                dict_barang[barang[data]] += int(jumlah[data])
    teks = f"""------------ DATA INVENTARIS ------------
{'barang'.center(25)} {'jumlah'.center(10)}
----------------------------------------
"""
    for key, value in dict_barang.items():
        teks += f"{key.center(25)} {str(value).center(10)}\n"
    return teks

def inventaris():
    while True:
        try:
            global listLaporan
            Clear_terminal()
            if len(listLaporan) <= 0:
                print('Tidak Ada Laporan Untuk Saat Ini')
                return input("Klik Enter Untuk Melanjutkan")
            print(List_Inventaris())
            inputan = int(input(f'Pilih 1-{len(listLaporan)} atau {len(listLaporan)+1} untuk kembali : '))-1
            if inputan <= len(listLaporan)-1 and inputan >= 0:
                while True:
                    try:
                        Clear_terminal()
                        print(inventaris_Daerah(inputan))
                        inputan2 = int(input(f'Pilih 1-{len(remove_keys(listLaporan)[inputan]['data'])} atau {len(remove_keys(listLaporan)[inputan]['data'])+1} untuk kembali: '))-1
                        if inputan2 <= len(remove_keys(listLaporan)[inputan]['data'])-1:
                            data = remove_keys(listLaporan)[inputan]['data'][inputan2]
                            barang = data['Jenis Barang'].split(";")
                            jumlahBarang = data['Jumlah Barang'].split(";")
                            TeksBarang = ''
                            for i in range(len(barang)):
                                if i == len(barang)-1:
                                    TeksBarang += f'    - {barang[i]} ({jumlahBarang[i]})'
                                else:
                                    TeksBarang += f'    - {barang[i]} ({jumlahBarang[i]})\n'
                            teks = f"""✦ ═══════════════════════【 DETAIL LAPORAN 】═══════════════════════ ✦
⊳ ID Laporan: {data['ID']} 
⊳ Tanggal: {data['Tanggal']}
⊳ Daerah: {data['Daerah']}
⊳ Barang: 
{TeksBarang}
⊳ Alasan: {data['Alasan']} 

✦ ══════════════════════════════════════════════════════════════════ ✦"""
                            if data['status'] == 'acc' or data['status'] == 'reject':
                                Clear_terminal()
                                input(teks + '\nKlik enter untuk melanjutkan')
                                break
                            teks = f"{data_daerah(data['Daerah'])}\n\n{teks}"
                            Clear_terminal()
                            print(teks)
                            inputan = int(input(f"""1. Acc
2. Reject
3. Kembali
✦ Masukkan Angka: """))
                            if inputan == 1:
                                Id = data['ID']
                                daerah = data['Daerah']
                                data = pd.read_csv('./laporan.csv')
                                data.loc[data['ID'] == Id, 'status'] = 'acc'
                                data.loc[data['ID'] == Id, 'respon'] = None
                                data.to_csv('./laporan.csv', index=False)
                                input('sukses acc laporan')
                                break
                            elif inputan == 2:
                                alasan = input('masukkan alasan: ')
                                Id = data['ID']
                                data = pd.read_csv('./laporan.csv')
                                data.loc[data['ID'] == Id, 'status'] = 'reject'
                                data.loc[data['ID'] == Id, 'respon'] = alasan
                                data.to_csv('./laporan.csv', index=False)
                                input('sukses menolak laporan')
                                break
                            else:
                                break
                        else:
                            break
                    except (ValueError)  :
                        Clear_terminal()
                        input(error('Pilihan yang Anda masukkan tidak valid. Harap masukkan angka yang benar.'))
            else:
                listLaporan = {}
                break
            listLaporan = {}
        except (ValueError)  :
            Clear_terminal()
            input(error('Pilihan yang Anda masukkan tidak valid. Harap masukkan angka yang benar.'))
            listLaporan = {}