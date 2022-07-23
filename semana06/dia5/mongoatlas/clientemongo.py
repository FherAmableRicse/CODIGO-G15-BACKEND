from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))

db_codigo = cliente['db_codigo']

colAlumno = db_codigo['alumno']

"""
dicNuevoAlumno = {
  
    "id" : 4,
    "nombre":  "carlos paredes4",
    "email" : "carlosparedes1@gmail.com",
    "celular": "9989123454",
    "github": "https://github.com/cparedes4"
}

nuevoAlumnoId = colAlumno.insert_one(dicNuevoAlumno)

print("Nuevo alumno " + str(nuevoAlumnoId))
"""
for alumno in colAlumno.find():
    print(alumno['nombre'] + ' - ' + alumno['email'] + ' - ' + alumno['celular'])