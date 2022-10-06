from Conversor import *
while True:
  try:
    valor= float(input('Digite o valor em centímetros: '))
    break
  except:
    continue
conversao(valor)