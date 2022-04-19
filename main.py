from art import logo
print(logo)
print()

def soma(x, y):
  """Soma dois elementos"""
  return (x + y)

def sub (x, y):
  """Subtrai dois elementos"""
  return (x - y)

def mul (x, y):
  """Multiplica dois elementos"""
  return (x * y)

def div (x, y):
  """Divide dois elementos"""
  return (x / y)

operacao = {
  
  "+":soma,
  "-":sub,
  "*":mul,
  "/":div
}

def calculator():
  x = int(input("Insira o número x: "))
  for simbol in operacao:
    print(simbol)
  
  flag = True
  
  while flag: 
    escolher_operacao = input("Escolha uma operação: ")
    y = int(input("Insira o próximo número: "))
    calculo = operacao[escolher_operacao]
    resposta = calculo(x, y)
    print(f"{x} {escolher_operacao} {y} = {resposta}")
  
  
  
    if input(f"Se quiser continuar calculando com {resposta} digite Y: ") == "Y":
      x = resposta
  
    else:
      flag = False
      calculator()
  


calculator()
