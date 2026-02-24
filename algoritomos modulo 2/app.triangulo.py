from geometriaplana import eh_triangulo, obter_tipo_triangulo
from utils_oi import escrever, obter_inteiro
from areatiangulo import area_triangulo


def main():
  escrever('*** App Triângulo ***')

  lado_1 = obter_inteiro('Lado 1: ')
  lado_2 = obter_inteiro('Lado 2: ')
  lado_3 = obter_inteiro('Lado 3: ')

  if eh_triangulo(lado_1, lado_2, lado_3):
    tipo = obter_tipo_triangulo(lado_1, lado_2, lado_3)
    escrever(f'SIM. Os lados formam um Triângulo {tipo} com area {area_triangulo}.')
    # Heron
  else:
    escrever('NÃO. Os lados não formam um triângulo.')

main()