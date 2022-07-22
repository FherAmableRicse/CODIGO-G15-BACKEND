from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

db_codigo = cliente['db_codigo']

colAlumno = db_codigo['alumno']

"""
dicNuevoAlumno = {
  
    "id" : 2,
    "nombre":  "carlos paredes",
    "emai" : "carlosparedes@gmail.com",
    "celular": "9989123452",
    "github": "https://github.com/cparedes"
}

nuevoAlumnoId = colAlumno.insert_one(dicNuevoAlumno)

print("Nuevo alumno " + str(nuevoAlumnoId))
"""
for alumno in colAlumno.find():
    print(alumno['nombre'] + ' - ' + alumno['email'] + ' - ' + alumno['celular'])