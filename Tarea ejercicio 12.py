a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))


diferencia = abs(a - b)


if diferencia % 2 == 0:
    print("La suma de los dígitos de los números es:", sum(int(d) for d in str(a)) + sum(int(d) for d in str(b)))


elif diferencia in [2, 3, 5, 7]:
    print("El producto de los números es:", a * b)


elif str(diferencia)[-1] == '4':
    print("Los dígitos de los números son:")
    for d in str(a):
        print(d)
    for d in str(b):
        print(d)

else:
    print("No se cumple ninguna de las condiciones")