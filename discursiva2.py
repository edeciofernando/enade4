import numpy as np

MAX = 4
# Cria um array com "max" elementos (vazios) do tipo Unicode String com até 20 caracteres
caminhoneiros = np.empty(MAX, dtype="<U20")
total = None

def inicializa():
  global total
  total = 0

def estaVazia():
  if total == 0:
    return True
  else:
    return False

def estaCheia():
  if total >= MAX:
    return True
  else:
    return False

def enfileirar(caminhoneiro):
  if not estaCheia():
    global total 
    total = total + 1
    # posição é total-1, pois em Python (e outras linguagens), o array inicia em 0
    caminhoneiros[total-1] = caminhoneiro
  else:
    print("Fila cheia")

# Questão 1
def desenfileirar():
  if estaVazia():
    removido = "Fila vazia"
  else:
    global total
    total = total - 1
    removido = caminhoneiros[0]  
    for i in range(total):
      caminhoneiros[i] = caminhoneiros[i+1]
  return removido

# Questão 2
def mostrarFila():
  if estaVazia():
    print("Fila vazia")
  else:
    print("Caminhoneiros na Fila")
    for i in range(total):
      print(caminhoneiros[i])

# -------------------------------------- Programa principal

inicializa()
while True:
  print("\nMenu Principal")
  print("-"*30)
  print("1. Enfileirar")
  print("2. Desenfileirar")
  print("3. Mostrar Fila")
  print("4. Sair")
  opcao = int(input("Opção: "))
  if opcao == 1:
    nome = input("Caminhoneiro: ")
    enfileirar(nome)
  elif opcao == 2:
    nome = desenfileirar()
    print(nome)
  elif opcao == 3:
    mostrarFila()
  else:
    break
