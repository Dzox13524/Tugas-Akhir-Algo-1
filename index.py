import pandas as pd
import os

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')



while True:
    print("""
            1. Login
            2. Registrasi
            3. Keluar
            """)
    input('Memilih yang mana: ')
    if input == '1':
        