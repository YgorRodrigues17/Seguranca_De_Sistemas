//INSTALAR O "NODE" E O "EXPRESS"
//EXECUTAR COM "NODE SERVER.JS"


const fs = require('fs')
const path = require('path')
const https = require('https')
const express = require('express')
const port = 443 //PORTA PADRÃO CONEXÕES HTTPS
const app = express()


app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, '/index.html'))
})

https.createServer({
    key: fs.readFileSync('key.pem'), //LE A CHAVE PRIVADA GERADA
    cert: fs.readFileSync('cert.pem') //LE A CHAVE DO CERTIFICADO
}, app).listen(port)
console.log('https://localhost:' + port)