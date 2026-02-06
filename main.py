num1 = float(input())
num2 = float(input())

print(num1 + num2)

continuar = input("¿Quieres usar la calculadora avanzada? (s/n): ")

if continuar.lower() == "s":

    print("\n--- Calculadora extendida ---")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Módulo")

    opcion = input("Elige una opción: ")

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", a + b)

    elif opcion == "2":
        print("Resultado:", a - b)

    elif opcion == "3":
        print("Resultado:", a * b)

    elif opcion == "4":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("No se puede dividir entre 0")

    elif opcion == "5":
        print("Resultado:", a % b)

    else:
        print("Opción no válida")



