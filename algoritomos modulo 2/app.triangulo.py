def main():
 escrever("*** app triangulo***")

 lado1 = obterinteiro("lado 1: ")
 lado2 = obterinteiro("lado 2: ")
 lado3 = obterinteiro("lado 3: ")

 resultado= verifircar_se_eh_triangulo(lado1, lado2, lado3)

 if resultado == True:
  escrever("SIM. Os lados forem um triangulo.")
 else:
  escrever("NAO. Os lados foram un triangulo.")









  

main()