import random

letras = ["d", "f", "w", "i", "o", "e", "h", "f", "w", "i", "f", "h"]

A = int(input("¿Que tan larga quieres que sea tu contraseña0? (responder con numeros)"))
P = " "

for i in range(A):
    M = random.choice(letras)
    P += M
print("Tu contraseña es", P)