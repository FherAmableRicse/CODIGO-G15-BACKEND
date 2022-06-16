from tabulate import tabulate

table = [
    ["fher","fher@gmail.com",9991921921],
    ["fher","fher@gmail.com",9991921921]
 ]
columnas = ["nombre", "email", "celular"]
print(tabulate(table,headers = columnas,tablefmt="grid"))