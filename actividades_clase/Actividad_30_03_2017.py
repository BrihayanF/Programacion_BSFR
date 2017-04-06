numero="654983533242987"
sumas=0
longitud=len(numero)
if longitud == 1:
    sumas=0
else:
    while longitud>1:
        sumas=sumas+1
        suma=0
        for i in numero:
            suma=suma+int(i)
            longitud=len(str(suma))
            #print(longitud)
            numero=str(suma)
            print(numero)
print("Las sumas son: "+str(suma))
#segundo programa
contactos=[]
file= open("file.txt","r")
for i in file:
    registros= i.split(",")
    contactos.append(registros)
for j in contactos:
    print(j)
def Nombre (dato):
    for k in contactos:
        if k [0]== dato:
            print("Esta interezado: "+k[3])
x=Nombre("Brihayan")
print(x)