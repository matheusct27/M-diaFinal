

print("--------Média IFCE--------\n")
name = input("Qual o seu nome?: ")

def calculate_total_average():
  print()

  primeira_n1 = float(input("digite sua 1° nota da n1: "))
  segunda_n1 = float(input("digite sua 2° nota da n1: "))
  n1_média = (primeira_n1 + segunda_n1) / 2

  print()

  primeira_n2 = float(input("digite sua 1° nota da n2: "))
  segunda_n2 = float(input("digite sua 2° nota da n2: "))
  n2_média = (primeira_n2 + segunda_n2) / 2

  print()

  final_média = (n1_média * 2 + n2_média * 3) / 5

  if final_média < 6:
    AF = float(input("digite sua nota da AF: "))
    final_média = (final_média + AF) / 2

  print()
  print(f"{name}, sua média final: ")

  if final_média >= 6:
    print(final_média)
  else:
    print("você não passou")

  print()
  print("Você deseja recalcular sua nota?")
  print("1.S          2.N")
  continuar_resposta = int(
    input("digite o número que representa sua resposta: "))

  if continuar_resposta == 1:
    return True
  return False

while True:
  contine = calculate_total_average()

  if contine == False:
    break
  print()
