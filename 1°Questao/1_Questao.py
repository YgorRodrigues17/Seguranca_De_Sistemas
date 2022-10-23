from turtle import clear
import rsa

#CUIDADO VISTO QUE TRABALHA COM OPEN E WRITE AO EXECUTAR CODIGO DESTA MANEIRA DARA ERRO POIS OS ARQUIVOS JA FORAM CRIADOS, PARA CONSEGUIR EXECUTA-LO, COMENTE AS LINHAS 9, 10, 13, 14

public_key, private_key = rsa.newkeys(1024)

#CRIA ARQUIVO GERANDO A CHAVE PUBLICA
with open('public.pem', 'wb') as f:
    f.write(public_key.save_pkcs1('PEM'))

#CRIA ARQUIVO GERANDO A CHAVE PRIVADA
with open('private.pem', 'wb') as f:
    f.write(private_key.save_pkcs1('PEM'))

#abre o arquivo que contem a chave publica para ser utilizada na criptografia
with open('public.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

#abre o arquivo que contem a chave privada para ser utilizada na descriptografia
with open('private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

#informa a mensagem que deseja enviar
message = 'enviando mensagem criptografada'

#criptografa a mensagem
encrypted_message = rsa.encrypt(message.encode(), public_key)

#abre a mensagem criptografa para ser desciptografada
encrypted_message = open('encrypted.message', 'rb').read()

#descriptografa a mensagem utilizando a chave privada e em seguida escreve na tela
clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())

#cria arquivo com mensagem criptografada
#with open('encrypted.message', 'wb') as f:
 #   f.write(encrypted_message)