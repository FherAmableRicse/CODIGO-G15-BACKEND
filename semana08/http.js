const http = require('http');

http.createServer(function(req,res){
    console.log('servidor web iniciando');
    console.log(req.url);

    switch(req.url){
        case '/hola':
            res.write('estas en la pagina hola');
            res.end();
            break;
        default:
            res.write('<h1><center>Mi primer servidor web con NodeJs</center></h1>')
            res.end();
    }
}).listen(5000);