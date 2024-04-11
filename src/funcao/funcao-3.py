import cowsay
import random

def console_divertido(texto):
    funcoes = [
        cowsay.cow,
        cowsay.dragon,
        cowsay.turtle,
        cowsay.tux
    ]

    funcao = random.choice(funcoes)
    funcao(texto)

console_divertido("Eae, python!!! mu, mu, mu")

#def console_divertido(texto):
#   cowsay.tux(texto)

# console_divertido("Eae, python!!! mu, mu, mu")


