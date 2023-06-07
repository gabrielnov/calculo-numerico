import sympy
import numpy as np

def lagrange(n, x, y):    
    poly = 0
    for i in range(n):
        termo = y[i]
        for j in range(n):
            if j != i:
                termo *= (sympy.Symbol('x') - x[j]) / (x[i] - x[j])
        poly += termo
    return str(sympy.expand(poly))

def newton(n, x, y):
    # Cálculo das diferenças divididas
    # Inicializando a tabela das diferenças divididas
    dd = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dd[i][0] = y[i]
    # Cálculo das diferenças divididas de ordem 1, 2, ..., n-1
    for j in range(1, n):
        for i in range(n-j):
            dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (x[i+j] - x[i])
    # Construção do polinômio
    def f(t):
        res = dd[0][0]
        prod = 1
        for j in range(1, n):
            prod *= (t - x[j-1])
            res += dd[0][j] * prod
        return res
    return f

def sistemas(n, X, Y):
    matriz_A = np.zeros((n, n))
    vetor_b = np.zeros(n)

    for i in range(n):
        for j in range(n):
            matriz_A[i][j] = X[i] ** (n - j - 1)

        vetor_b[i] = Y[i]

    coeficientes = np.linalg.solve(matriz_A, vetor_b)

    # Construir a representação em forma de polinômio
    polinomio = ""
    for i in range(n):
        if coeficientes[i] != 0:
            if i != n - 1:
                polinomio += f"{coeficientes[i]:.15f}*x**{n - i - 1} + "
            else:
                polinomio += f"{coeficientes[i]:.15f}"
    
    return polinomio

def opcao():
  print("\nSelecione o metodo para calcular o polinomio interpolador:" 
        + "\n1) Sistemas lineares" 
        + "\n2) Lagrange"
        + "\n3) Newton"
        + "\n4) Todos os metodos")
  
  opt = input("\nOpcao: ")
  while opt not in ["1","2","3", "4"]:
    print("Opcao invalida, tente novamente digitando 1, 2, 3 ou 4...\n")
    opt = input("Opcao: ")

  return opt

def main():
  n = int(input("Digite o número de pontos a serem interpolados: "))
  X = []
  Y = []

  print("!!! Atencao: digitar os valores decimais usando ponto (.) Exemplo: 52.032 !!!\n")
  for i in range(n):
    try:
        x = float(input(f"Digite o valor de x{i}: "))
        X.append(x)
        y = float(input(f"Digite o valor de f(x{i}): "))
        Y.append(y)
    except:
      print("Fatal error: valor digitado incorretamente. Reiniciando aplicacao...\n\n")
      main()
      
  x = float(input("Informe o valor do x a ser calculado: "))
  
  opt = opcao()

  if opt == "1":
    polinomio = sistemas(n, X, Y)
  if opt == "2":
    polinomio = lagrange(n, X, Y)
  if opt == "3":
    polinomio = lagrange(n, X, Y)
    f = newton(n, X, Y)
    print(f"\nPolinomio: P(x) = {polinomio}")
    print(f"\nResultado P({x}) = {f(x):.6f}")
    return
  if opt == "4":
    poli1 = sistemas(n, X, Y)
    res1 = eval(poli1)
    
    poli2 = lagrange(n, X, Y)
    res2 = eval(poli2)

    f = newton(n, X, Y)
    res3 = f(x)
    
    print(f"\nResolucao de sistemas: \nP(x) = {poli1}\nP({x}) = {res1}")
    print(f"\nLagrange: \nP(x) = {poli2}\nP({x}) = {res2}")
    print(f"\nNewton: \nP(x) = {poli2}\nP({x}) = {res3}")
    
    return
    
  print(f"\nPolinomio: P(x) = {polinomio}")
  resultado = eval(polinomio)
  print(f"\nResultado: P({x}) = {resultado:.6f}")

if __name__ == "__main__":
  main()


  
