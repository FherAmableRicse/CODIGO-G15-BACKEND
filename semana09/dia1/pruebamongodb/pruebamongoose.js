const mongoose = require('mongoose');

async function main(){
    //conexion a la bd 
    await mongoose.connect('mongodb://localhost:27017/db-mongoose');

    const PeliculSchema = new mongoose.Schema({
        nombre:String,
        fecha: {type:Date,default:Date.now},
        rating:{type:Number,required:[true,'necesita un rating']}
    });

    const Pelicula = mongoose.model('col_pelicula', PeliculSchema);

    const drama =  new Pelicula({nombre:'los chotanos',rating:10});
    await drama.save();

    // const pelicula2 = new Pelicula({nombre:'Rapidos y furiosos'});
    // await pelicula2.save();

    const listadoPeliculas = await Pelicula.find();
    console.log(listadoPeliculas);
}
main().catch(err=>console.log(err));