valor = int(input("¿Qué valor quieres convertir en metros? "))

print("""
      \nSelecciona una de las siguientes opciones
      -------------------------------------------
      1)De metros a pies
      2)De metros a pulgadas
      3)De metros a Yardas
      -------------------------------------------
      """)
conversion = int(input("Selecciona una opción: "))
if conversion == 1:
    resultado = valor * 3.28084
    print("El resultado es: ", resultado)
elif conversion == 2:
    resultado = valor * 39.37008
    print("El resultado es: ", resultado)
elif conversion == 3:
    resultado = valor * 1.093613
    print("El resultado es: ", resultado)
else:
    print("Error de sintaxis, valor no corresponde a las respuestas dadas")