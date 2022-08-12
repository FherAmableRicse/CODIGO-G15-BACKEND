const {Router} = require('express');
const router = Router();

const {getAll,create} = require('../controllers/usuario.controller');

router.route('/')
      .get(getAll)
      .post(create)

module.exports = router;