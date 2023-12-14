import os
os.system('cls')
print("Bienvenido al juego del ahorcado, tienes 3 intentos para pasar")
mensajes = "Fundamentos"
contenedor = list(mensajes)
Contador = 0
Verificador = False
Resultado = mensajes
for item in enumerate(mensajes):
    mensajes = (mensajes.replace(item, "-", 1))
print(f"la cantidad de letras que tiene la siguiente oracion es de: {len(mensajes)}")
print(mensajes)
intentos = 0
tiempo =0
while(Verificador != True):
    comparador = input("inserte una letra que considera esta en la palabra")
    definicion = int(Resultado.count(comparador))
    if definicion != 0:
        print("Felicidades encontraste una letra")
        for item in contenedor:
            tiempo+=0
            if comparador == item:
                mensajes = (mensajes.replace("-", item, tiempo))
    
    if definicion == 0:
        intentos += 1
    if intentos == 3:
        Verificador= True
        

    