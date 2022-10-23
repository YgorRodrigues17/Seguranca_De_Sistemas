from inspect import signature
import rsa

#CUIDADO, NÃO DESCOMENTAR AS LINHAS 9, 10, 13, 14, 32, 33, FORAM UTILIZADAS NO INICIO DA CONSTRUÇÃO DO CODIGO PARA GERAR AS CHAVES, SE DESCOMENTAR DARA ERRO

#public_key, private_key = rsa.newkeys(1024)

#criar arquivo com chave publica
#with open('public.pem', 'wb') as f:
 #   f.write(public_key.save_pkcs1('PEM'))

#cria arquivo com chave privada
#with open('private.pem', 'wb') as f:
 #   f.write(private_key.save_pkcs1('PEM'))


#abre o arquivo que contem a chave publica para ser utilizada na criptografia
with open('public.pem', 'rb') as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

#abre o arquivo que contem a chave privada para ser utilizada na descriptografia
with open('private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

#informa a mensagem que deseja assinar
message = 'arquivo assinado digitalmente'

#atribui a variavel assinatura a mensagem sendo assinada digitalmente utilizando a chave privada
signature = rsa.sign(message.encode(), private_key, 'SHA-256')

#cria arquivo assinado
#with open('mensagem_assinado', 'wb') as f:
  #  f.write(signature)

with open('mensagem_assinado', 'rb') as f:
    signature = f.read()

print(rsa.verify(message.encode(), signature, public_key))   

#SE O RESULTADO FOR IGUAL A 'SHA-256' SIGNIFICA QUE A MENSAGEM É VALIDA
#SE ALTERAR QUALQUER LETRA  DENTRO DA MENSAGEM O PROGRAMA IRA DAR ERRO "VERIFICATION FAILED"
