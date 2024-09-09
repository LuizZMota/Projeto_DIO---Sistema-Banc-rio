limite = 500
saldo = 0
num_saques = 0
lim_saques = 3
saque = 0
deposito_total = 0
total_saque = 0

def depositar():
  global saldo, deposito_total
  deposito = 0
  while True:    
    deposito = float(input("Insira um valor para depositar: "))
    if deposito<0:
      print("Valor inválido.")
    else:
      saldo+=deposito
      deposito_total+=deposito
      break
  

def sacar():
  global lim_saques, total_saque, saldo
  if lim_saques == 0:
    print("Número de saques diários excedidos.")
    return
  else:
    while True:
      saque = float(input("Insira um valor para sacar (limite de até 500 reais): "))
      if saque>saldo:
        print("Saldo insuficiente.")
      elif saque>limite:
        print("Este valor excedeu o limite de 500 reais por saldo.")
      else:
        lim_saques-=1
        saldo-=saque
        total_saque+=saque
        break
  
def extrato():
  print(f"Valor total depositado: R${deposito_total:,.2f}")
  print(f"Valor total sacado: R${total_saque:,.2f}")
  print(f"Valor total na conta: R${saldo:,.2f}")



while True:
  opcao = 0
  print("1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Sair")
  opcao = int(input("Insira uma opção: "))
  if opcao == 1:
    depositar()
  elif opcao == 2:
    sacar()
  elif opcao == 3:
    extrato()
  elif opcao == 4:
    print("Saindo...")
    break
  else:
    print("Opção inválida.")