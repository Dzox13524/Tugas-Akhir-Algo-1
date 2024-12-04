import os
import subprocess

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
    