# 1. Define unha lista de 5 nomes, unha lista de números e unha lista de 5 elementos de distintos tipos en python.

lista_nombres = ["Martin", "Juan", "Antonio", "Maria", "Jaime", "Clara"]
lista_numeros = [1,2,3,4,5]
lista_tipos = [1,"Martin", 10.4, True, ["Lista",3,"elementos"]]

def listar_bucle(lista):
    for elemento in lista:
        print(elemento)

# 2. Define unha tupla de 5 nomes, unha tupla de números e unha tupla de 5 elementos de distintos tipos en python.

tupla_nombres = ("Martin", "Juan", "Antonio", "Maria", "Jaime", "Clara")
tupla_numeros = (1,2,3,4,5)
tupla_tipos = ("Martin", 1, 23.4, True, ("hola", 34, False))

# 3. Define un dicionario de 5 nomes e idades en python.

diccionario_datos = {'Martin': 25, 'Maria': 26, 'Pedro': 21, 'Mario': 12, "Jesus": 64}
def listar_diccionario(diccionario):
    for nombre, edad in diccionario.items():
        print(f"Nombre: {nombre}, edad: {edad}")

# 4. Escribe un programa en Python que calcule a área dun triángulo dados a
#  base e a altura como entrada do usuario. Logo, calcula o perímetro do 
# triángulo sumando a lonxitude dos seus tres lados. Finalmente, imprime 
# ambos os resultados redondeados a dous decimais.

def calcular_area_triangulo(base,altura):
    area = (base * altura) / 2
    print(f"Área del triangulo de base {base} y altura {altura} es: {round(area,2)}")

def calcular_perimetro_triangulo(base, altura):
    lado_a = base/2
    lado_b = altura
    hipotenusa = ((lado_a**2) + (lado_b**2))**0.5
    perimetro = hipotenusa*2 + base
    print(f"El perímetro para un triangulo de base {base} y altura {altura} es {round(perimetro,2)}")

# 5. Escribe un programa en Python que determine se un número ingresado 
# polo usuario é par ou impar. Se o número é par, imprime "O número é par",
#  pola contra, imprime "O número é impar".
def par_impar(numero):
    if numero %2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")


# 6. Escribe un programa en Python que sume os primeiros 10 números 
# naturais (do 1 ao 10) e imprima o resultado.

def sumar_primeros_numeros(numero):
    acum = 0
    for i in range(numero +1):
        acum += i
    print(f"La suma de los {numero} primeros numeros naturales es: {acum}")

# 8. Escribe un programa en Python que verifique si un número ingresado 
# polo usuario é positivo e par.

def numero_positivo_par(numero):
    if numero > 0:
        if numero %2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    else:
        print("El numero debe ser positivo")

def numero_positivo_par2(numero):
    if numero >0 and numero %2 == 0:
        print("El número es positivo y par")
    else:
        print("El número no cumple los requisitos")

# 9. Escribe un programa en Python que cree unha clase Miclase con un 
# método saludar que imprime “¡Hola! soy un objeto de la clase Miclase.”
#  Posteriormente instancia un obxecto da clase Miclase e chama a función 
# saludar do obxecto creado

class Miclase :
    def __init__(self):
        self
    
    def saludar(self):
        print("¡Hola! soy un objeto de la clase Miclase.")

def fibonacci(n): 
    if n <= 1: 
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 

if __name__ == "__main__":
    #Ejercicio 1
    # print(lista_nombres)
    # listar_bucle(lista_nombres)

    # Ejercicio 2
    # print(tupla_nombres)
    # listar_bucle(tupla_tipos)

    # Ejercicio 3
    # print(diccionario_datos)
    # listar_diccionario(diccionario_datos)

    # Ejercicio 4
    # base_triangulo = float(input("Ingresa base triangulo"))
    # altura_triangulo = float(input("Ingresa altura triangulo"))
    # calcular_area_triangulo(base_triangulo, altura_triangulo)
    # calcular_perimetro_triangulo(base_triangulo, altura_triangulo)

    # Ejercicio 5
    # par_impar(5)
    # par_impar(10)

    #Ejercicio 6
    # sumar_primeros_numeros(10)

    # Ejercicio 7
    # numero_positivo_par(10)
    # numero_positivo_par(5)
    # numero_positivo_par(-1)
    # numero_positivo_par2(10)
    # numero_positivo_par2(5)
    # clase = Miclase()
    # clase.saludar()
    resultado = fibonacci(0)
    print(f"Resultado fibonacci es: {resultado}")
