M = int(input("Digite seu peso atual: "))
H = float(input("Digite sua altura atual: "))

IMC = M/(H**2)

if IMC < 18:
  m = (18* H**2) -  M 
  print (f"Magreza, você necessita engordar {m} Kg para ficar no estado normal")

if IMC >=18 and IMC < 24,999999999999:
  print ("Normal")

if IMC >= 25 and IMC <29,99999999999:
  m = M - (18* H**2)
  print (f"Sobrepeso, você necessita engordar {m} Kg para ficar no estado normal")

if IMC >= 30 and IMC < 39,99999999999:
  m = M - (18* H**2)
  print (f"Obesidade, você necessita engordar {m} Kg para ficar no estado normal")

if IMC >= 40:
  m = M - (18* H**2)
  print(f"Obesidade Mórbida, você necessita engordar {m} Kg para ficar no estado normal")
