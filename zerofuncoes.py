# pip install py-expression-eval

from __future__ import division

import math
import random
import re

funcao = ""

def f(expr, porc, x):
  expr = expr + "-" + str(porc)
  expr = expr.replace("^","**")
  expr = expr.replace("e","2.718281828")
  
  return eval(expr)

def bisseccao(a, b, tol, porc, expr):
  x, fx = 0, 0
  iter = 0

  while abs(b - a) > tol:
    x = (a + b) / 2.0
    fx = f(expr, porc, x)
    if f(expr, porc, a) * fx < 0:
      b = x
    else:
      a = x
    iter += 1

  raiz = (a + b) / 2.0

  return raiz

def secante(x0, x1, eps, porc, expr):
  fx0 = f(expr, porc, x0)
  fx1 = f(expr, porc, x1)
  x2, fx2 = 0.0, 0.0
  d = abs(x1 - x0)
  while d > eps:
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    fx2 = f(expr, porc, x2)
    d = abs((x2 - x1) / x2)
    x0 = x1
    fx0 = fx1
    x1 = x2
    fx1 = fx2
  return x2

def calcula():
    opcao = 0
    print("Digite o método desejado")

    print("1 - Bissecção")
    print("2 - Secante")
    opcao = int(input("Opção: "))
    while opcao != 1 and opcao != 2:
        print("Digite a opção desejada")
        print("1 - Bissecção")
        print("2 - Secante")
        opcao = int(input("Opção: "))

    expr = input("Digite a função F(x). Exemplo: x^2 + e^(-5) : ")

    a, b, eps = 0, 0, 0
    

    print(
    "\nNível de erro\n\nPara 10 elevado a -2, por exemplo, digite 1e-2\nPara 10 elevado a -5, digite 1e-5\n"
    )
    
    eps = float(input("Digite o nível de erro máximo: "))
  
    porcA = float(input("Digite a primeira porcentagem (exemplo: 10): "))/100
    porcB = float(input("Digite a segunda porcentagem (exemplo: 10): "))/100
    print("\n")
    print("Intervalo [a, b]")
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    if opcao == 1:
        raizA = bisseccao(a, b, eps, porcA, expr)
        print("Raiz A = {:.7f}".format(raizA))
        a = float(input("Digite o  valor de 'a': "))
        b = float(input("Digite o valor de 'b': "))
        raizB = bisseccao(a, b, eps, porcB, expr)

    else:
        # Calcula a raiz utilizando o método da secante
        raizA = secante(a, b, eps, porcA, expr)
        print("Raiz A = {:.7f}".format(raizA))
        a = float(input("Digite o valor de 'a': "))
        b = float(input("Digite o valor de 'b': "))
        raizB = secante(a, b, eps, porcB, expr)

    # Imprime o resultado
    print("Raiz B = {:.7f}".format(raizB))
    print("tempo de subida: {:.7f}".format(abs(raizA - raizB))) #tempo de subida 4.22

#para 10% -> 1.1023 com a e b sendo 1.1 1.2
#para 90% -> 5.3281 com a e b sendo 5 6
#funcao 1-(1+T+(T^2)/2)*e(-T)

def main():
    calcula()
    
if __name__ == "__main__":
    main()
