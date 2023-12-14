mensaje = "Fundamentos de programacion"
Vocal = int(0)
count = int(0)
lsvocales ='a,e,i,o,u'
for item in mensaje:
    if item in lsvocales:
        Vocal += 1
    else:
        count += 1
print(f"la cantidad de letras que hay en el mensaje es de: {len(mensaje)}")
print(f"la cantidad de vocales son: {Vocal}")
print(f"la cantidad de consonantes son: {count}")
print("ok")