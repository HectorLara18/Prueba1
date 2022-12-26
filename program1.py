import datetime

##Funciones
def master(loginName):
    if(loginName == "Hector Lara"):
        print("Welcome Master")
    else:
        print("welcome " + loginName)

_datetime = datetime.datetime.now()

if(2023 <= _datetime.year):
    print("esta caduco")
else:
    print("Aun sirve")

print(_datetime)
_entrada = input("Ingresa tu nombre: ")
master(_entrada)