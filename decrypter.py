import os ## importa o sistema operacional
import pyaes ## importa a bibliotéea de criptografia

# abre o arquivo criptografado
file_name = "arquivo.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# chave para descriptografia
key = b"cybersecuritydio"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remove o arquivo criptografado
os.remove(file_name)

# cria o arquivo descriptografado
new_file = "arquivo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()