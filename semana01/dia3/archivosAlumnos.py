import os
alumnos = []
if(os.path.isfile('alumnos.csv')):
    archivoAlumnos = open('alumnos.csv','r')
else:
    archivoAlumnos = open('alumnos.csv', 'w')
    archivoAlumnos.write('fher amable, fher@gmail.com,999999')
    archivoAlumnos.write('\nana lopez, ana@gmail.com, 991919191')
    archivoAlumnos.write('\njorge perez, jorge@gmail.com, 92222222')

strAlumnos = archivoAlumnos.read()
# print(strAlumnos)
archivoAlumnos.close()

lstAlumnos = strAlumnos.splitlines()
print(lstAlumnos)
for l in lstAlumnos:
     alumnoData = l.split(",")
     print(alumnoData)
     dictAlumnos = {
      'nombre':alumnoData[0],
      'email':alumnoData[1],
      'celular':alumnoData[2]
     }
     alumnos.append(dictAlumnos)