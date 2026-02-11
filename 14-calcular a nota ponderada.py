#Entrada 

n1=int(input("Qual a primeira nota do aluno?"))

n2=int(input("Qual a segunda nota do aluno?"))

n3=int(input("Qual a terceira nota do aluno?"))

p1=int(input("Qual o peso da primeira nota?"))

p2=int(input("Qual o peso da segunda nota?"))

p3=int(input("Qual o peso da terceira nota?"))

#Processamento

nota=(n1 * p1) + (n2 * p2) + (n3 * p3)

peso= p1 + p2 +p3

notafinal= nota / peso

#saida

print(f"A media ponderada sera de:{notafinal}")