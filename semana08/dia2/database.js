const mysql = require('mysql');

const mysqlconnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'db_codigo_g15'
})

mysqlconnection.connect(function(err){
    if(err){
        console.error(err);
        return;
    }
    else{
        console.log('conexion a bd exitosa');
    }
});

module.exports = mysqlconnection;

/*connection.query("select count(*) as total from tbl_alumno",function(error,results,fields){
    if(error) throw error;
    console.log('total de alumnos', results[0].total);
});

connection.end();*/
