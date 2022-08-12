const usuarioController = {};

const usuarioModel = require('../models/usuario.model');

usuarioController.getAll = async (req,res) =>{
    const usuarios = await usuarioModel.find();
    res.json({
        status:true,
        content:usuarios
    });
}

usuarioController.create = async (req,res) =>{
    const {nombre,password} = req.body;
    const nuevoUsuario = new usuarioModel({
        nombre,
        password
    })
    await nuevoUsuario.save();
    res.json({
        status:true,
        content:nuevoUsuario
    });
}


module.exports = usuarioController;